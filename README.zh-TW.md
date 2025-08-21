<p align="center">
    <img src="assets/banner.svg" alt="ipscan banner" width="100%" />
</p>

<div align="center">

# ipscan

快速 IP 掃描器 — 多線程 Ping 與 ARP（Windows）

[![PyPI 版本](https://img.shields.io/pypi/v/ipscan?logo=pypi&label=PyPI)](https://pypi.org/project/ipscan/)
![Python](https://img.shields.io/pypi/pyversions/ipscan?logo=python)
![OS](https://img.shields.io/badge/OS-Windows-blue?logo=windows)
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

- 多線程高速掃描
- 支援 Ping 與 ARP，API 簡潔
- 進度條與清晰輸出
- 相依套件少、易於安裝

## 效能說明

- Ping：/24 子網數秒內完成（依硬體而異）
- ARP：在本地網路極快

## 系統需求

- Python 3.7+
- Windows / Linux / macOS 皆可；Linux/macOS 使用系統工具（ip/arp/arping）

## 參與貢獻

歡迎提交 Issue 與 PR；如果覺得實用，請幫忙點個 Star！

---

<div align="center">
Made with ❤️ for network tinkerers.
</div>
