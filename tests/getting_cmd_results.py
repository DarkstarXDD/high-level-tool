import re
import subprocess

# Run ipconfig command
output_1 = subprocess.check_output(["ipconfig", "/all"]).decode("utf-8")
# print(output_1)


# Define regular expression pattern to match IPv4 address
hostname_pattern = r"Host Name[.\s]+: (.+)"
ipv4_pattern = r"IPv4 Address[.\s]+: ([\d.]+)"
ipv6_pattern = r"IPv6 Address[.\s]+: ([\da-fA-F:]+)"


# Search for Hostname address in the output
match = re.search(hostname_pattern, output_1)

if match:
    hostname = match.group(1)
    print(f"Hostname: {hostname}")
else:
    print("Hostname Address not found")


# Search for IPv4 address in the output
match = re.search(ipv4_pattern, output_1)

if match:
    ipv4_address = match.group(1)
    print(f"IPv4 Address: {ipv4_address}")
else:
    print("IPv4 Address not found")


# Search for IPv6 address in the output
match = re.search(ipv6_pattern, output_1)

if match:
    ipv6_address = match.group(1)
    print(f"IPv6 Address: {ipv6_address}")
else:
    print("IPv6 Address not found")


def get_mac_address():
    try:
        output = subprocess.check_output(["ipconfig", "/all"], universal_newlines=True)
        # Split the output into sections for each adapter
        adapters_info = output.split("\n\n")
        for adapter_info in adapters_info:
            # Check if the adapter is connected
            if (
                "Media State . . . . . . . . . . . : Media disconnected"
                not in adapter_info
            ):
                # Extract MAC address from the adapter information
                mac_match = re.search(
                    r"Physical Address[ .:]+([0-9A-Fa-f-]+)", adapter_info
                )
                if mac_match:
                    return mac_match.group(1)
        return None
    except subprocess.CalledProcessError:
        print("Error: Failed to execute ipconfig command.")
        return None


mac_address = get_mac_address()
if mac_address:
    print("MAC Address:", mac_address)
else:
    print("Unable to retrieve MAC address.")
