<p align="center">
	<img src="assets/banner.svg" alt="ipscan banner" width="100%" />
</p>

<div align="center">

# ipscan

Scanner IP rápido — Ping e ARP multithread (Windows)

[![PyPI](https://img.shields.io/pypi/v/ipscan?logo=pypi&label=PyPI)](https://pypi.org/project/ipscan/)
![Python](https://img.shields.io/pypi/pyversions/ipscan?logo=python)
![OS](https://img.shields.io/badge/OS-Windows-blue?logo=windows)
![Licença](https://img.shields.io/github/license/Wing9897/ipscan?color=success)

Idioma:
[English](README.md) · [繁體中文](README.zh-TW.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Español](README.es.md) · [Português BR](README.pt-BR.md) · [Русский](README.ru.md)

</div>

---

## Sumário

- Início rápido
- Funcionalidades
- Ferramentas CLI
- API Python
- Desempenho
- Requisitos
- Contribuição

---

## Início rápido

Instalar via PyPI:

```bash
pip install ipscan
```

### CLI

```bash
fping           # ping contínuo de alta velocidade (interativo)
sping           # varredura por ping
sarp            # varredura por ARP
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

## Funcionalidades

- Multithread para alta velocidade
- Ping e ARP com API simples
- Barra de progresso e saída limpa
- Poucas dependências

## Desempenho

- Ping: /24 em poucos segundos (depende do hardware)
- ARP: muito rápido na LAN

## Requisitos

- Python 3.7+
- Windows / Linux / macOS suportados; no Linux/macOS usa ferramentas do sistema (ip/arp/arping)

## Contribuição

Issues e PRs são bem-vindos. Se gostou, deixe uma ⭐.

---

<div align="center">
Made with ❤️ for network tinkerers.
</div>
