<p align="center">
	<img src="https://raw.githubusercontent.com/Wing9897/ipscan/main/assets/banner.svg" alt="ipscan banner" width="100%" />
</p>

<div align="center">

# ipscan

Scanner IP veloce — Ping e ARP multithread (Windows)

[![PyPI](https://img.shields.io/pypi/v/ipscan?logo=pypi&label=PyPI)](https://pypi.org/project/ipscan/)
![Python](https://img.shields.io/pypi/pyversions/ipscan?logo=python)
![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blue)
![Licenza](https://img.shields.io/github/license/Wing9897/ipscan?color=success)

Lingua:
[English](README.md) · [繁體中文](README.zh-TW.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Español](README.es.md) · [Português BR](README.pt-BR.md) · [Русский](README.ru.md)

</div>

---

## Indice

- Avvio rapido
- Funzionalità
- Strumenti CLI
- API Python
- Prestazioni
- Requisiti
- Contribuire

---

## Avvio rapido

Installazione da PyPI:

```bash
pip install ipscan
```

### CLI

```bash
fping           # ping continuo ad alta velocità (interattivo)
sping           # scansione intervallo via ping
sarp            # scansione intervallo via ARP
```

### API Python

Ping:

```python
from ipscan import ping_range, PingScanner

online_hosts = ping_range("192.168.1.1", "192.168.1.254")

scanner = PingScanner(timeout=1.0)
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

ARP:

```python
from ipscan import arp_range, ArpScanner

host_info = arp_range("192.168.1.1", "192.168.1.254")
for ip, mac in host_info.items():
		print(f"{ip} -> {mac}")

scanner = ArpScanner()
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

## Funzionalità

- Scansione multithread ad alta velocità
- Ping e ARP con API semplici
- Barra di avanzamento e output pulito
- Poche dipendenze

## Prestazioni

- Ping: /24 in pochi secondi (dipende dall'hardware)
- ARP: molto veloce in LAN

## Requisiti

- Python 3.7+
- Windows / Linux / macOS supportati; su Linux/macOS usa strumenti di sistema (ip/arp/arping)

## Contribuire

Issue e PR benvenuti. Se ti piace, lascia una ⭐.

---

<div align="center">
Made with ❤️ for network tinkerers.
</div>
