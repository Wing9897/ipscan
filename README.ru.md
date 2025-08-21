<p align="center">
	<img src="assets/banner.svg" alt="ipscan banner" width="100%" />
</p>

<div align="center">

# ipscan

Быстрый IP-сканер — многопоточный Ping и ARP (Windows)

[![PyPI](https://img.shields.io/pypi/v/ipscan?logo=pypi&label=PyPI)](https://pypi.org/project/ipscan/)
![Python](https://img.shields.io/pypi/pyversions/ipscan?logo=python)
![OS](https://img.shields.io/badge/OS-Windows-blue?logo=windows)
![Лицензия](https://img.shields.io/github/license/Wing9897/ipscan?color=success)

Языки:
[English](README.md) · [繁體中文](README.zh-TW.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Español](README.es.md) · [Português BR](README.pt-BR.md) · [Русский](README.ru.md)

</div>

---

## Содержание

- Быстрый старт
- Возможности
- CLI-инструменты
- Python API
- Производительность
- Требования
- Участие

---

## Быстрый старт

Установка из PyPI:

```bash
pip install ipscan
```

### CLI

```bash
fping           # высокоскоростной непрерывный ping (интерактив)
sping           # скан диапазона по ping
sarp            # скан диапазона по ARP
```

### Python API

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

## Возможности

- Многопоточное сканирование с высокой скоростью
- Поддержка Ping и ARP, простой API
- Прогресс-бар и чистый вывод
- Минимум зависимостей

## Производительность

- Ping: /24 за считанные секунды (зависит от железа)
- ARP: очень быстро в локальной сети

## Требования

- Python 3.7+
- Поддерживаются Windows / Linux / macOS; на Linux/macOS используются системные утилиты (ip/arp/arping)

## Участие

Issues и PR приветствуются. Если проект полезен — поставьте ⭐.

---

<div align="center">
Made with ❤️ for network tinkerers.
</div>
