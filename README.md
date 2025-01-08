# netissuestools

netissuestools 是一個網路工具，用於進行一些網路上的檢查。

## 功能

- **導入庫**：使用 import netissuestools
- **函式庫例子**：netissuestools.Superfast_multithread_ping.main()
- **直接使用 cmd 指令**：sfastping

其原理是進行多線程的 ping 功能，能在約 1 分鐘內完成對 65535 個 IP 的檢查。

## 安裝

可以使用 pip 安裝：

pip install netissuestools

## 例子

from netissuestools import Superfast_multithread_ping

Superfast_multithread_ping.main()
