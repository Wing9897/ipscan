<p align="center">
    <img src="https://raw.githubusercontent.com/Wing9897/ipscan/main/assets/banner.svg" alt="ipscan banner" width="100%" />
</p>

<div align="center">

# ipscan

快速 IP 掃描器 — 跨平台多線程 Ping 與 ARP 掃描（Windows、Linux、macOS）

[![PyPI 版本](https://img.shields.io/pypi/v/ipscan?logo=pypi&label=PyPI)](https://pypi.org/project/ipscan/)
![Python](https://img.shields.io/pypi/pyversions/ipscan?logo=python)
![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blue)
![授權](https://img.shields.io/github/license/Wing9897/ipscan?color=success)

語言：
[English](README.md) · [繁體中文](README.zh-TW.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Español](README.es.md) · [Português BR](README.pt-BR.md) · [Русский](README.ru.md)

</div>

---

## 目錄

- 快速開始
- 功能特色
- 命令列工具
- Python API 範例
- 效能說明
- 系統需求
- 參與貢獻

---

## 快速開始

從 PyPI 安裝：

```bash
pip install ipscan
```

**Windows 用戶**：安裝可選的 Windows 優化 ping 支援：
```bash
pip install "ipscan[windows]"
```

**注意**：Linux ARP 掃描需要 sudo 權限以獲得最佳效能。

### 命令列

```bash
fping           # 高速連續 Ping（互動式）
sping           # 範圍 Ping 掃描
sarp            # ARP 範圍掃描
```

### Python API

Ping 掃描：

```python
from ipscan import ping_range, PingScanner

online_hosts = ping_range("192.168.1.1", "192.168.1.254")

scanner = PingScanner(timeout=1.0)
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

ARP 掃描：

```python
from ipscan import arp_range, ArpScanner

host_info = arp_range("192.168.1.1", "192.168.1.254")
for ip, mac in host_info.items():
        print(f"{ip} -> {mac}")

scanner = ArpScanner()
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

## 功能特色

- **跨平台支援**：Windows、Linux、macOS 自動偵測作業系統
- **多線程掃描**：高速並發操作
- **智慧實現**：針對平台優化以獲得最佳效能
  - Windows：原生 SendARP API + ping3 函式庫
  - Linux：直接 scapy ARP 封包 + 系統 ping
  - macOS：系統 arp + ping 命令
- **簡單 API**：跨平台統一介面
- **進度追蹤**：即時進度條與清晰輸出

## 平台詳細資訊

| 功能 | Windows | Linux | macOS |
|------|---------|-------|---------|
| **Ping 掃描** | ping3 函式庫 | 系統 ping | 系統 ping |
| **ARP 掃描** | SendARP API | scapy 封包 | arp 命令 |
| **權限需求** | 無需特殊權限 | ARP 需要 sudo | 無需特殊權限 |
| **效能** | 優化 | 優化 | 良好 |
## 使用範例

### Linux ARP 掃描（需要 sudo）
```bash
sudo sarp
# 提示時輸入 IP 範圍
```

### 高速連續 ping
```bash
fping
# 輸入目標 IP 和間隔
```

### 範圍 ping 掃描
```bash
sping
# 輸入起始和結束 IP 地址
```

## 系統需求

- **Python 3.7+**
- **跨平台支援**：Windows、Linux、macOS
- **相依性**：
  - `tqdm`（進度條）
  - `scapy`（ARP 封包生成）
  - `ping3`（Windows 優化，可選）

## 參與貢獻

歡迎提交 Issue 與 PR；如果覺得實用，請幫忙點個 Star！

---

<div align="center">
Made with ❤️ for network tinkerers.
</div>
