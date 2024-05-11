import socket
import psutil


class GeneralData:
    def __init__(self):

        self.hostname = socket.gethostname()

        if self.get_data():
            self.ipv4_address = self.get_data()["ipv4_address"]
            self.ipv6_address = self.get_data()["ipv6_address"]
            self.mac_address = self.get_data()["mac_address"]

        else:
            self.ipv4_address = "-"
            self.ipv6_address = "-"
            self.mac_address = "-"

        # print(f"IPv4 Address: {self.ipv4_address}")
        # print(f"IPv6 Address: {self.ipv6_address}")
        # print(f"MAC Address: {self.mac_address}")

    def get_data(self):
        interfaces = psutil.net_if_addrs()

        for interface, addresses in interfaces.items():

            # Check whether the interface is NOT a loopback interface
            not_loopback = interface != "Loopback Pseudo-Interface 1"

            # Check whether the interface is up and running
            is_up = psutil.net_if_stats()[interface].isup

            if not_loopback and is_up:
                ipv4_address = None
                ipv6_address = None
                mac_address = None

                # Loop over all the addresses (not loopback & up and running) in the interface
                for address in addresses:
                    if (
                        address.family == socket.AF_INET
                        and not address.address.startswith("169.254")
                    ):
                        ipv4_address = address.address

                    elif address.family == socket.AF_INET6:

                        if not ipv6_address and not address.address.startswith("fe80"):
                            ipv6_address = address.address

                    elif address.family == psutil.AF_LINK:
                        mac_address = address.address

                if ipv4_address or ipv6_address or mac_address:
                    return {
                        "ipv4_address": ipv4_address,
                        "ipv6_address": ipv6_address,
                        "mac_address": mac_address,
                    }

        return None


GeneralData()
