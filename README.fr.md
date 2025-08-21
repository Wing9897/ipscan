<p align="center">
	<img src="assets/banner.svg" alt="ipscan banner" width="100%" />
</p>

<div align="center">

# ipscan

Scanner IP rapide — Ping & ARP multithread (Windows)

[![PyPI](https://img.shields.io/pypi/v/ipscan?logo=pypi&label=PyPI)](https://pypi.org/project/ipscan/)
![Python](https://img.shields.io/pypi/pyversions/ipscan?logo=python)
![OS](https://img.shields.io/badge/OS-Windows-blue?logo=windows)
![Licence](https://img.shields.io/github/license/Wing9897/ipscan?color=success)

Langue :
[English](README.md) · [繁體中文](README.zh-TW.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Español](README.es.md) · [Português BR](README.pt-BR.md) · [Русский](README.ru.md)

</div>

---

## Sommaire

- Démarrage rapide
- Fonctionnalités
- Outils CLI
- API Python
- Performances
- Prérequis
- Contribution

---

## Démarrage rapide

Installer via PyPI :

```bash
pip install ipscan
```

### CLI

```bash
fping           # ping continu haute vitesse (interactif)
sping           # scan de plage par ping
sarp            # scan de plage ARP (Windows)
```

### API Python

Ping :

```python
from ipscan import ping_range, PingScanner

online_hosts = ping_range("192.168.1.1", "192.168.1.254")

scanner = PingScanner(timeout=1.0)
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

ARP :

```python
from ipscan import arp_range, ArpScanner

host_info = arp_range("192.168.1.1", "192.168.1.254")
for ip, mac in host_info.items():
		print(f"{ip} -> {mac}")

scanner = ArpScanner()
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

## Fonctionnalités

- Multithread pour une grande vitesse
- Ping et ARP, API simple
- Barre de progression, sortie claire
- Peu de dépendances

## Performances

- Ping : /24 en quelques secondes (selon le matériel)
- ARP : très rapide sur le LAN (Windows uniquement)

## Prérequis

- Python 3.7+
- Windows (requis pour ARP)

## Contribution

Issues & PR bienvenus. Une ⭐ est appréciée.

---

<div align="center">
Made with ❤️ for network tinkerers.
</div>
