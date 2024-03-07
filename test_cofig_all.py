import re
import subprocess

# Run ipconfig command
output_1 = subprocess.check_output(["ipconfig", "/all"]).decode("utf-8")
output_2 = subprocess.check_output(["route", "print"]).decode("utf-8")

# Define regular expression patterns
hostname_pattern = r"Host Name[.\s]+: (.+)"
ipv4_pattern = r"IPv4 Address[.\s]+: ([\d.]+)"
ipv6_pattern = r"IPv6 Address[.\s]+: ([\da-fA-F:]+)"
r_ipv4_pattern = r"Default Gateway\s*:\s*([\d.]+)"
r_ipv6_pattern = r"Default Gateway\s*:\s*([a-fA-F\d:]+)"

# Search for IPv4 address in the output
match = re.search(ipv4_pattern, output_1)
ipv4_address = match.group(1) if match else None

# Search for IPv6 address in the output
match = re.search(ipv6_pattern, output_1)
ipv6_address = match.group(1) if match else None

# Search for hostname in the output
match = re.search(hostname_pattern, output_1)
hostname = match.group(1) if match else None

# Search for Router IPv4 address in the output
match = re.search(r_ipv4_pattern, output_1)
r_ipv4 = match.group(1) if match else None

# Search for Router IPv6 address in the output
match = re.search(r_ipv6_pattern, output_1)
r_ipv6 = match.group(1) if match else None

# Print results
print(f"Hostname: {hostname}")
print(f"IPv4 Address: {ipv4_address}")
print(f"IPv6 Address: {ipv6_address}")
print(f"Router IPv4 Address: {r_ipv4}")
print(f"Router IPv6 Address: {r_ipv6}")
