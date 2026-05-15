<p align="center">
	<img src="https://raw.githubusercontent.com/Wing9897/ipscan/main/assets/banner.svg" alt="ipscan banner" width="100%" />
</p>

<div align="center">

# ipscan

고속 IP 스캐너 — 크로스 플랫폼 멀티스레드 Ping/ARP 스캔 (Windows, Linux, macOS)

[![PyPI](https://img.shields.io/pypi/v/ipscan?logo=pypi&label=PyPI)](https://pypi.org/project/ipscan/)
![Python](https://img.shields.io/pypi/pyversions/ipscan?logo=python)
![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blue)
![License](https://img.shields.io/github/license/Wing9897/ipscan?color=success)

언어:
[English](README.md) · [繁體中文](README.zh-TW.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Español](README.es.md) · [Português BR](README.pt-BR.md) · [Русский](README.ru.md)

</div>

---

## 목차

- 빠른 시작
- 기능
- CLI 도구
- Python API 예제
- 성능 안내
- 요구 사항
- 기여

---

## 빠른 시작

PyPI 설치:

```bash
pip install ipscan
```

### CLI

```bash
fping           # 고속 연속 ping (대화형)
sping           # ping 범위 스캔
sarp            # ARP 범위 스캔
```

### Python API

Ping 스캔:

```python
from ipscan import ping_range, PingScanner

online_hosts = ping_range("192.168.1.1", "192.168.1.254")

scanner = PingScanner(timeout=1.0)
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

ARP 스캔:

```python
from ipscan import arp_range, ArpScanner

host_info = arp_range("192.168.1.1", "192.168.1.254")
for ip, mac in host_info.items():
		print(f"{ip} -> {mac}")

scanner = ArpScanner()
results = scanner.scan_range("10.0.0.1", "10.0.0.100")
```

## 기능

- 멀티스레드 기반 고속 스캔
- Ping/ARP 지원, 간결한 API
- 진행 표시 및 깔끔한 출력
- 의존성 최소화

## Linux 설정 (권장)

Linux에서 최고 성능을 위해 Python에 raw socket 권한을 부여하세요:

```bash
# 고속 Ping 스캔 활성화 (raw ICMP socket, ~100배 빠름)
sudo setcap cap_net_raw+ep $(readlink -f $(which python3))

# 고속 Ping + ARP 스캔 활성화
sudo setcap cap_net_raw,cap_net_admin+ep $(readlink -f $(which python3))
```

미설정 시:
- **Ping 스캔**은 작동하지만 subprocess로 폴백 (느림)
- **ARP 스캔**은 `sudo`가 필요

권한 복원 (제거):
```bash
sudo setcap -r $(readlink -f $(which python3))
```

> **참고**: Python 설치당 한 번만 설정하면 됩니다. virtualenv 사용 시 venv의 Python에 대해 실행하세요.

## 성능 안내

- Ping: /24 몇 초 내 스캔(환경에 따라 다름)
- ARP: 로컬 네트워크 매우 빠름

## 요구 사항

- Python 3.7+
- Windows / Linux / macOS 지원; Linux/macOS는 시스템 도구(ip/arp/arping) 사용

## 기여

Issue/PR 환영합니다. 유용했다면 Star 부탁드립니다.

---

<div align="center">
Made with ❤️ for network tinkerers.
</div>
