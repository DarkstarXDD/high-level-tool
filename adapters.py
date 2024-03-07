import subprocess
import re

# Run ipconfig command and get the output
output = subprocess.check_output(["ipconfig", "/all"], text=True)

# Split the output by adapter sections
adapter_sections = re.split(r"\r\n\r\n", output)

# Create a list to store information of each adapter
adapters = []

# Define regular expression pattern to extract adapter description
description_pattern = r"(?:Ethernet|Wireless LAN) adapter (.*?):"

# Define regular expressions to extract adapter information
adapter_info_patterns = {
    "Description": description_pattern,
    "Physical Address": r"Physical Address\s*:\s*(.*?)\r\n",
    "IPv4 Address": r"IPv4 Address.*?:(.*?)\r\n",
    "IPv6 Address": r"IPv6 Address.*?:(.*?)\r\n",
    "Default Gateway": r"Default Gateway.*?:(.*?)\r\n",
}

# Extract information for each adapter
for section in adapter_sections:
    adapter_info = {}
    for key, pattern in adapter_info_patterns.items():
        match = re.search(pattern, section)
        if match:
            adapter_info[key] = match.group(1).strip()
    adapters.append(adapter_info)

# Print information for each adapter
for i, adapter in enumerate(adapters, start=1):
    print(f"Adapter {i}:")
    for key, value in adapter.items():
        print(f"{key}: {value}")
    print()
