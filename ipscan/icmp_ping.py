"""
Linux 原始 ICMP socket ping 實作模組

使用 raw ICMP socket 直接發送/接收 ICMP Echo Request/Reply 封包，
避免 subprocess 的 fork+exec 開銷，大幅提升 Linux 上的 ping 效能。

需要 root 權限或 cap_net_raw 能力才能使用 raw socket。
"""

import os
import struct
import socket
import time
import threading
from typing import Optional, Tuple


# 模組層級權限快取
_permission_cache: Optional[bool] = None
_permission_cache_lock = threading.Lock()

# ICMP 常數
ICMP_ECHO_REQUEST = 8  # Echo Request type
ICMP_ECHO_REPLY = 0    # Echo Reply type
ICMP_CODE = 0          # Code for Echo Request/Reply
ICMP_HEADER_SIZE = 8   # ICMP header size in bytes
IP_HEADER_SIZE = 20    # Standard IP header size in bytes
DEFAULT_PAYLOAD = b'\x00' * 56  # 56 bytes payload (standard ping size)


def _calculate_checksum(data: bytes) -> int:
    """計算 ICMP checksum (RFC 1071)

    將資料視為 16-bit 整數序列進行加總，
    若資料長度為奇數則補零，最後取反碼。

    Args:
        data: 要計算 checksum 的位元組資料

    Returns:
        16-bit checksum 值
    """
    if len(data) % 2 == 1:
        data += b'\x00'

    checksum = 0
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i + 1]
        checksum += word

    # 將進位加回低 16 位
    checksum = (checksum >> 16) + (checksum & 0xFFFF)
    checksum += (checksum >> 16)

    # 取反碼
    return ~checksum & 0xFFFF


def _build_echo_request(identifier: int, sequence: int,
                        payload: bytes = DEFAULT_PAYLOAD) -> bytes:
    """建構 ICMP Echo Request 封包

    封包格式:
    - Type (1 byte): 8 (Echo Request)
    - Code (1 byte): 0
    - Checksum (2 bytes): 計算後填入
    - Identifier (2 bytes): 用於匹配 request/reply
    - Sequence Number (2 bytes): 序列號
    - Payload (variable): 資料負載

    Args:
        identifier: 封包識別碼 (用於匹配回覆)
        sequence: 序列號
        payload: 資料負載

    Returns:
        完整的 ICMP Echo Request 封包 (bytes)
    """
    # 先用 checksum=0 建構 header 以計算 checksum
    header = struct.pack('!BBHHH',
                         ICMP_ECHO_REQUEST,  # Type
                         ICMP_CODE,          # Code
                         0,                  # Checksum (placeholder)
                         identifier,         # Identifier
                         sequence)           # Sequence Number

    # 計算 checksum
    checksum = _calculate_checksum(header + payload)

    # 重新建構 header，填入正確的 checksum
    header = struct.pack('!BBHHH',
                         ICMP_ECHO_REQUEST,
                         ICMP_CODE,
                         checksum,
                         identifier,
                         sequence)

    return header + payload


def _parse_echo_reply(data: bytes, expected_id: int) -> Optional[Tuple[int, int]]:
    """解析 ICMP Echo Reply 封包

    從接收到的原始封包中提取 ICMP Echo Reply 資訊。
    原始 socket 接收的資料包含 IP header (通常 20 bytes) + ICMP 封包。

    Args:
        data: 從 socket 接收的原始資料 (含 IP header)
        expected_id: 預期的識別碼 (用於匹配)

    Returns:
        若為有效的 Echo Reply 且 ID 匹配，回傳 (identifier, sequence)；
        否則回傳 None
    """
    if len(data) < IP_HEADER_SIZE + ICMP_HEADER_SIZE:
        return None

    # 取得 IP header 長度 (IHL 欄位，單位為 4 bytes)
    ip_header_length = (data[0] & 0x0F) * 4

    if len(data) < ip_header_length + ICMP_HEADER_SIZE:
        return None

    # 解析 ICMP header
    icmp_data = data[ip_header_length:]
    icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_seq = struct.unpack(
        '!BBHHH', icmp_data[:ICMP_HEADER_SIZE]
    )

    # 驗證是否為 Echo Reply 且 ID 匹配
    if icmp_type == ICMP_ECHO_REPLY and icmp_code == ICMP_CODE and icmp_id == expected_id:
        return (icmp_id, icmp_seq)

    return None


def has_raw_socket_permission() -> bool:
    """檢測是否有建立 raw ICMP socket 的權限

    嘗試建立 raw socket 來檢測權限。結果會在模組層級快取，
    避免每次 ping 都重新檢測。

    Returns:
        True 如果有權限建立 raw ICMP socket，否則 False
    """
    global _permission_cache

    # 快速路徑：已有快取結果
    if _permission_cache is not None:
        return _permission_cache

    with _permission_cache_lock:
        # Double-check pattern
        if _permission_cache is not None:
            return _permission_cache

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            sock.close()
            _permission_cache = True
        except (PermissionError, OSError):
            _permission_cache = False

    return _permission_cache


def raw_ping(target: str, timeout: float = 1.0) -> Tuple[bool, Optional[float]]:
    """使用原始 ICMP socket 對目標進行 ping

    建立獨立的 raw socket（確保執行緒安全），發送 ICMP Echo Request，
    等待 Echo Reply 並計算 RTT。

    Args:
        target: 目標 IP 地址字串
        timeout: 超時時間（秒）

    Returns:
        tuple(bool, Optional[float]):
            - (True, rtt_seconds) 如果收到回覆
            - (False, None) 如果超時或發生錯誤

    Raises:
        PermissionError: 如果沒有 raw socket 權限
    """
    # 使用 thread ID 和 process ID 組合作為 identifier，確保唯一性
    identifier = (os.getpid() ^ threading.current_thread().ident) & 0xFFFF
    sequence = 1

    # 每次呼叫建立獨立 socket（執行緒安全）
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    except (PermissionError, OSError) as e:
        raise PermissionError(
            "無法建立 raw ICMP socket，需要 root 權限或 cap_net_raw 能力"
        ) from e

    try:
        sock.settimeout(timeout)

        # 建構並發送 ICMP Echo Request
        packet = _build_echo_request(identifier, sequence)
        send_time = time.perf_counter()
        sock.sendto(packet, (target, 0))

        # 接收回覆
        while True:
            try:
                data, addr = sock.recvfrom(1024)
                recv_time = time.perf_counter()

                # 解析回覆
                result = _parse_echo_reply(data, identifier)
                if result is not None:
                    rtt = recv_time - send_time
                    return (True, rtt)

                # 收到的不是我們的回覆，檢查是否超時
                elapsed = recv_time - send_time
                if elapsed >= timeout:
                    return (False, None)

                # 調整剩餘超時時間
                remaining = timeout - elapsed
                sock.settimeout(remaining)

            except socket.timeout:
                return (False, None)

    except (OSError, socket.error):
        return (False, None)
    finally:
        sock.close()
