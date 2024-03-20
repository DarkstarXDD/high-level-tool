import psutil
import socket


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
            # Initialize variables to store IPv4, IPv6, and MAC addresses
            ipv4_address = None
            ipv6_address = None
            mac_address = None

            # Iterate over addresses of the interface
            for address in addresses:
                # Check if the address is an IPv4 private address
                if address.family == socket.AF_INET and not address.address.startswith(
                    "169.254"
                ):
                    ipv4_address = address.address
                # Check if the address is an IPv6 address
                elif address.family == socket.AF_INET6:
                    ipv6_address = address.address
                # Check if the address is a MAC address
                elif address.family == psutil.AF_LINK:
                    mac_address = address.address

            # Return IPv4, IPv6, and MAC addresses if found
            if ipv4_address or ipv6_address or mac_address:
                return {"IPv4": ipv4_address, "IPv6": ipv6_address, "MAC": mac_address}

    return None  # No private IP address found


# Call the function to retrieve network interface information
network_info = get_private_ip()

# Check if network information was found
if network_info:
    print("Private IP address:", network_info["IPv4"])
    print("IPv6 address:", network_info["IPv6"])
    print("MAC address:", network_info["MAC"])
else:
    print("No private IP address found.")
