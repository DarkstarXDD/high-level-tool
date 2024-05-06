import requests


def lookup_mac_vendor(mac_address):
    url = f"https://api.macvendors.com/{mac_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        elif response.status_code == 404:
            return "Vendor not found for the given MAC address."
        else:
            return f"Error: {response.status_code}"
    except requests.RequestException as e:
        return f"Error occurred: {e}"


# Example usage
mac_address = "hello"
vendor_info = lookup_mac_vendor(mac_address)
print(vendor_info)
