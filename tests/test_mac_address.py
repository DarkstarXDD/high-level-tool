import subprocess
import re


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
