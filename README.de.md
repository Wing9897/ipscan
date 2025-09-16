<p align="center">
	<img src="https://raw.githubusercontent.com/Wing9897/ipscan/main/assets/banner.svg" alt="ipscan banner" width="100%" />
</p>

<div align="center">

# ipscan

Schneller IP-Scanner — Multithreaded Ping & ARP (Windows)

[![PyPI](https://img.shields.io/pypi/v/ipscan?logo=pypi&label=PyPI)](https://pypi.org/project/ipscan/)
![Python](https://img.shields.io/pypi/pyversions/ipscan?logo=python)
![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blue)
![Lizenz](https://img.shields.io/github/license/Wing9897/ipscan?color=success)

Sprache:
[English](README.md) · [繁體中文](README.zh-TW.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Español](README.es.md) · [Português BR](README.pt-BR.md) · [Русский](README.ru.md)

</div>

---

## Inhalt

- Schnellstart
- Funktionen
- CLI-Tools
- Python-API
- Performance
- Anforderungen
- Beitrag leisten

---

## Schnellstart

Installation über PyPI:

```bash
pip install ipscan
```

### CLI

```bash
fping           # Hochgeschwindigkeits-Ping (interaktiv)
sping           # Bereichs-Ping-Scan
sarp            # ARP-Bereichsscan
```

### Python-API

Ping-Scan:

```python
from ipscan import ping_range, PingScanner

online_hosts = ping_range("192.168.1.1", "192.168.1.254")

scanner = PingScanner(timeout=1.0)
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

ARP-Scan:

```python
from ipscan import arp_range, ArpScanner

host_info = arp_range("192.168.1.1", "192.168.1.254")
for ip, mac in host_info.items():
		print(f"{ip} -> {mac}")

scanner = ArpScanner()
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

## Funktionen

- Multithreaded für hohe Geschwindigkeit
- Ping & ARP, einfache API
- Fortschrittsanzeige, saubere Ausgabe
- Wenige Abhängigkeiten

## Performance

- Ping: /24 in wenigen Sekunden (abhängig von Hardware)
- ARP: sehr schnell im lokalen Netzwerk

## Anforderungen

- Python 3.7+
- Windows / Linux / macOS unterstützt; unter Linux/macOS werden Systemtools (ip/arp/arping) verwendet

## Beitrag leisten

Issues & PRs willkommen. Über ein ⭐ würde ich mich freuen.

---

<div align="center">
Made with ❤️ for network tinkerers.
</div>
