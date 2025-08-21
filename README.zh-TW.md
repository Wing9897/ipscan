# ipscan

快速IP掃描工具 - 多線程 Ping 和 ARP 掃描（Windows）

語言：繁體中文 | English

• 目前頁面（繁中）
• 英文版請見：README.md

## 安裝

```bash
pip install ipscan
```

## 使用方法

### Ping 掃描

```python
from ipscan import ping_range, PingScanner

# 掃描 IP 範圍
online_hosts = ping_range("192.168.1.1", "192.168.1.254")
print(f"在線主機: {online_hosts}")

# 使用類接口
scanner = PingScanner(timeout=1.0)
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

### ARP 掃描

```python
from ipscan import arp_range, ArpScanner

# 掃描 IP 範圍並獲取 MAC 地址
host_info = arp_range("192.168.1.1", "192.168.1.254")
for ip, mac in host_info.items():
    print(f"{ip} -> {mac}")

# 使用類接口
scanner = ArpScanner()
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

### 命令行工具

```bash
# Ping 掃描
fping

# ARP 掃描
farp
```

## 特點

- 多線程掃描，速度極快（Ping 掃描 65535 個裝置約 30–60 秒；ARP 掃描約 15–30 秒）
- 支援 Ping 與 ARP 掃描
- 顯示進度條
- 簡潔的 API 設計

## 系統需求

- Python 3.7+
- Windows（ARP 掃描需要）
