import json
import psutil
import socket

interfaces = psutil.net_if_addrs().items()
# print(list(interfaces)[0])


def check_up(interface):
    if (
        interface != "Loopback Pseudo-Interface 1"
        and psutil.net_if_stats()[interface].isup
    ):
        return "Up"

    else:
        return "Down"


for interface, addresses in interfaces:
    for address in addresses:

        is_up = check_up(interface)

        if address.family == socket.AF_INET:
            print(f"{address.address}: True, {is_up}")
        else:
            print(f"{address.address}: False, {is_up}")

# interfaces = psutil.net_if_stats()
# print(interfaces["Ethernet"].isup)
