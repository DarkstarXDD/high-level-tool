import scapy.all as scapy
from tabulate import tabulate
import re

# Regular Expression Pattern to recognize IPv4 addresses.
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

# Get the address range to ARP
while True:
    ip_add_range_entered = input(
        "\nPlease enter the IP address and range that you want to send the ARP request to (e.g., 192.168.1.0/24): "
    )
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} is a valid IP address range")
        break

# Try ARPing the IP address range supplied by the user.
# The arping() method in scapy creates a packet with an ARP message
# and sends it to the broadcast MAC address ff:ff:ff:ff:ff:ff.
# If a valid IP address range was supplied, the program will return
# the list of all results.
arp_result = scapy.arping(ip_add_range_entered, verbose=False)

# Process the ARP result to extract MAC addresses and IP addresses
arp_table = []
for sent, received in arp_result[0]:
    arp_table.append([received.psrc, received.hwsrc])

arp_table_sorted = sorted(arp_table, key=lambda x: x[0])

# Display the ARP result in a table format
print(
    tabulate(
        arp_table_sorted,
        headers=["IP Address", "MAC Address"],
        tablefmt="grid",
    )
)
