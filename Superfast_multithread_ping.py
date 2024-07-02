import ping3
import threading
import ipaddress
import re

def valid_ip(ip):
    cutting_part = ip.split('.')
    if len(cutting_part) != 4:
        print('Is not ip format....app will be closed')
        exit()
    for part in cutting_part:
        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            print('Is not ip format....app will be closed')
            exit()
    return ip
    
def ping_host(ip_address):
    try:
        response_time = ping3.ping(str(ip_address))
        if response_time is not None and response_time is not False:
            print(f"{ip_address} is Online")
    except(ping3.errors.HostUnknown, ping3.errors.TimeExceeded):
        pass
        
def main():
    start_ip0 = input('Enter Starting IP: ')
    start_ip = valid_ip(start_ip0)
    end_ip0 = input('Enter End IP: ')
    end_ip = valid_ip(end_ip0)
    # 建立 IP 地址列表
    ip_addresses = [str(ipaddress.IPv4Address(ip)) for ip in range(int(ipaddress.IPv4Address(start_ip)), int(ipaddress.IPv4Address(end_ip)) + 1)]

    # 創建線程列表
    threads = []

    #ping 請求的線程
    for ip_address in ip_addresses:
        t = threading.Thread(target=ping_host, args=(ip_address,))
        threads.append(t)
        t.start()

    # 等待所有線程完成
    for t in threads:
        t.join()
    print("The End of the searching")
main()
