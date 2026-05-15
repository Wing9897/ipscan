<p align="center">
	<img src="https://raw.githubusercontent.com/Wing9897/ipscan/main/assets/banner.svg" alt="ipscan banner" width="100%" />
</p>

<div align="center">

# ipscan

Escáner IP rápido — Ping y ARP multihilo (Windows)

[![PyPI](https://img.shields.io/pypi/v/ipscan?logo=pypi&label=PyPI)](https://pypi.org/project/ipscan/)
![Python](https://img.shields.io/pypi/pyversions/ipscan?logo=python)
![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blue)
![Licencia](https://img.shields.io/github/license/Wing9897/ipscan?color=success)

Idioma:
[English](README.md) · [繁體中文](README.zh-TW.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Español](README.es.md) · [Português BR](README.pt-BR.md) · [Русский](README.ru.md)

</div>

---

## Contenido

- Inicio rápido
- Funciones
- Herramientas CLI
- API de Python
- Rendimiento
- Requisitos
- Contribuir

---

## Inicio rápido

Instalar desde PyPI:

```bash
pip install ipscan
```

### CLI

```bash
fping           # ping continuo de alta velocidad (interactivo)
sping           # escaneo de rango por ping
sarp            # escaneo de rango por ARP
```

### API de Python

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

## Funciones

- Escaneo multihilo de alta velocidad
- Ping y ARP con API simple
- Barra de progreso y salida clara
- Pocas dependencias

## Configuración Linux (recomendado)

Para mejor rendimiento en Linux, otorgar permisos de raw socket a Python:

```bash
# Habilitar escaneo Ping rápido (raw ICMP socket, ~100x más rápido)
sudo setcap cap_net_raw+ep $(readlink -f $(which python3))

# Habilitar escaneo Ping + ARP rápido
sudo setcap cap_net_raw,cap_net_admin+ep $(readlink -f $(which python3))
```

Sin esta configuración:
- **Escaneo Ping** funciona pero usa subprocess (más lento)
- **Escaneo ARP** requiere `sudo`

Restaurar (eliminar el permiso):
```bash
sudo setcap -r $(readlink -f $(which python3))
```

> **Nota**: Solo se necesita hacer una vez por instalación de Python. Con virtualenv, ejecutar sobre el binario Python del venv.

## Rendimiento

- Ping: /24 en segundos (según hardware)
- ARP: muy rápido en LAN

## Requisitos

- Python 3.7+
- Windows / Linux / macOS soportados; en Linux/macOS usa herramientas del sistema (ip/arp/arping)

## Contribuir

Issues y PRs bienvenidos. Si te gusta, deja una ⭐.

---

<div align="center">
Made with ❤️ for network tinkerers.
</div>
