import psutil
import socket

# loopback interface: a special interface that allows a computer to send network packets to itself


def get_private_ip():
    # Get all network interfaces
    interfaces = psutil.net_if_addrs()

    # Iterate over interfaces
    for interface, addresses in interfaces.items():
        # Check if the interface is not loopback and is up
        if (
            interface != "Loopback Pseudo-Interface 1"
            and psutil.net_if_stats()[interface].isup
        ):
            # Iterate over addresses of the interface
            for address in addresses:
                # Check if the address is an IPv4 private address
                if address.family == socket.AF_INET and not address.address.startswith(
                    "169.254"
                ):
                    return address.address

    return None  # No private IP address found


private_ip = get_private_ip()
if private_ip:
    print("Private IP address:", private_ip)
else:
    print("No private IP address found.")


# import json
# import psutil


# def format_network_interfaces():
#     interfaces = psutil.net_if_addrs()
#     formatted_interfaces = {}

#     for interface, addresses in interfaces.items():
#         formatted_addresses = []
#         for address in addresses:
#             formatted_addresses.append(
#                 {
#                     "family": address.family,
#                     "address": address.address,
#                     "netmask": address.netmask,
#                     "broadcast": address.broadcast,
#                 }
#             )
#         formatted_interfaces[interface] = formatted_addresses

#     return formatted_interfaces


# formatted_data = format_network_interfaces()
# print(json.dumps(formatted_data, indent=4))


# import json
# import psutil


# def format_network_interfaces():
#     interfaces = psutil.net_if_addrs()
#     return interfaces


# formatted_data = format_network_interfaces()
# print(json.dumps(formatted_data, indent=4))
