<p align="center">
	<img src="assets/banner.svg" alt="ipscan banner" width="100%" />
</p>

<div align="center">

# ipscan

快速 IP 扫描器 — 多线程 Ping 与 ARP（Windows）

[![PyPI](https://img.shields.io/pypi/v/ipscan?logo=pypi&label=PyPI)](https://pypi.org/project/ipscan/)
![Python](https://img.shields.io/pypi/pyversions/ipscan?logo=python)
![OS](https://img.shields.io/badge/OS-Windows-blue?logo=windows)
![License](https://img.shields.io/github/license/Wing9897/ipscan?color=success)

语言：
[English](README.md) · [繁體中文](README.zh-TW.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Español](README.es.md) · [Português BR](README.pt-BR.md) · [Русский](README.ru.md)

</div>

---

## 目录

- 快速开始
- 功能特色
- 命令行工具
- Python API 示例
- 性能说明
- 系统要求
- 参与贡献

---

## 快速开始

从 PyPI 安装：

```bash
pip install ipscan
```

### 命令行

```bash
fping           # 高速连续 Ping（交互式）
sping           # 范围 Ping 扫描
sarp            # ARP 范围扫描（Windows）
```

### Python API

Ping 扫描：

```python
from ipscan import ping_range, PingScanner

online_hosts = ping_range("192.168.1.1", "192.168.1.254")

scanner = PingScanner(timeout=1.0)
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

ARP 扫描：

```python
from ipscan import arp_range, ArpScanner

host_info = arp_range("192.168.1.1", "192.168.1.254")
for ip, mac in host_info.items():
		print(f"{ip} -> {mac}")

scanner = ArpScanner()
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

## 功能特色

- 多线程高速扫描
- 支持 Ping 与 ARP，API 简洁
- 进度条与清晰输出
- 依赖少，易安装

## 性能说明

- Ping：/24 子网数秒内完成（随硬件而异）
- ARP：本地网极快（仅 Windows）

## 系统要求

- Python 3.7+
- Windows（ARP 功能需要）

## 参与贡献

欢迎提交 Issue 与 PR；如果觉得实用，请点 Star！

---

<div align="center">
Made with ❤️ for network tinkerers.
</div>
