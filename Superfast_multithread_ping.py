import ping3
import threading
import ipaddress

def ping_host(ip_address):
    try:
        response_time = ping3.ping(str(ip_address))
        if response_time is not None and response_time is not False:
            print(f"{ip_address} is Online")
    except (ping3.errors.HostUnknown, ping3.errors.TimeExceeded):
        pass

# 定義 IP 範圍
start_ip = ipaddress.IPv4Address("192.168.0.0")
end_ip = ipaddress.IPv4Address("192.168.50.255")

# 建立 IP 地址列表
ip_addresses = [ipaddress.IPv4Address(ip) for ip in range(int(start_ip), int(end_ip) + 1)]

# 創建線程列表
threads = []

# 啟動 ping 請求的線程
for ip_address in ip_addresses:
    t = threading.Thread(target=ping_host, args=(ip_address,))
    threads.append(t)
    t.start()

# 等待所有線程完成
for t in threads:
    t.join()
