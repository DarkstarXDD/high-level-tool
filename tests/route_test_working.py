import subprocess
import re


def get_gateway_ip():
    try:
        output = subprocess.check_output(["route", "print"]).decode("utf-8")
        gateway_ipv4 = re.search(r"0.0.0.0\s+0.0.0.0\s+(\d+\.\d+\.\d+\.\d+)", output)
        gateway_ipv6 = re.search(r"::/0\s+::/0\s+([\da-fA-F:]+)", output)
        if gateway_ipv4:
            return gateway_ipv4.group(1)
        elif gateway_ipv6:
            return gateway_ipv6.group(1)
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None


# Usage
gateway_ip = get_gateway_ip()
if gateway_ip:
    print("Gateway IP:", gateway_ip)
else:
    print("Failed to retrieve the gateway IP address.")
