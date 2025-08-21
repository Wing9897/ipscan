<p align="center">
	<img src="assets/banner.svg" alt="ipscan banner" width="100%" />
</p>

<div align="center">

# ipscan

高速 IP スキャナ — マルチスレッド Ping / ARP（Windows）

[![PyPI](https://img.shields.io/pypi/v/ipscan?logo=pypi&label=PyPI)](https://pypi.org/project/ipscan/)
![Python](https://img.shields.io/pypi/pyversions/ipscan?logo=python)
![OS](https://img.shields.io/badge/OS-Windows-blue?logo=windows)
![License](https://img.shields.io/github/license/Wing9897/ipscan?color=success)

言語：
[English](README.md) · [繁體中文](README.zh-TW.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Español](README.es.md) · [Português BR](README.pt-BR.md) · [Русский](README.ru.md)

</div>

---

## 目次

- クイックスタート
- 機能
- CLI ツール
- Python API サンプル
- パフォーマンス
- 動作要件
- コントリビュート

---

## クイックスタート

PyPI からインストール：

```bash
pip install ipscan
```

### CLI

```bash
fping           # 高速連続 ping（対話式）
sping           # ping 範囲スキャン
sarp            # ARP 範囲スキャン
```

### Python API

Ping スキャン：

```python
from ipscan import ping_range, PingScanner

online_hosts = ping_range("192.168.1.1", "192.168.1.254")

scanner = PingScanner(timeout=1.0)
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

ARP スキャン：

```python
from ipscan import arp_range, ArpScanner

host_info = arp_range("192.168.1.1", "192.168.1.254")
for ip, mac in host_info.items():
		print(f"{ip} -> {mac}")

scanner = ArpScanner()
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

## 機能

- マルチスレッドで高速スキャン
- Ping / ARP をサポート、シンプルな API
- 進行バーつきの分かりやすい出力
- 依存が少なく導入が容易

## パフォーマンス

- Ping：/24 を数秒でスキャン（環境による）
- ARP：ローカルネットワークで非常に高速

## 動作要件

- Python 3.7+
- Windows / Linux / macOS をサポート（Linux/macOS は ip/arp/arping を利用）

## コントリビュート

Issue / PR を歓迎します。気に入ったら Star をお願いします。

---

<div align="center">
Made with ❤️ for network tinkerers.
</div>
