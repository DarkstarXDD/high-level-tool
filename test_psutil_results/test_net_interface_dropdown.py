import psutil
import tkinter as tk
from tkinter import ttk


def get_network_interfaces():
    """Retrieve a list of network interfaces."""
    interfaces = psutil.net_if_addrs()
    return [
        interface
        for interface in interfaces.keys()
        if interface != "Loopback Pseudo-Interface 1"
    ]


def interface_selected(event):
    """Callback function for when a network interface is selected."""
    selected_interface = interface_dropdown.get()
    display_interface_data(selected_interface)


def display_interface_data(interface):
    """Display essential data related to the selected network interface."""
    addresses = psutil.net_if_addrs().get(interface, [])
    for address in addresses:
        # Display the data for the selected interface (e.g., IP addresses, MAC addresses, etc.)
        print(address)


# Create Tkinter window
root = tk.Tk()
root.title("Network Interface Information")

# Create dropdown menu for network interfaces
interfaces = get_network_interfaces()
interface_label = tk.Label(root, text="Select Network Interface:")
interface_label.pack()
interface_dropdown = ttk.Combobox(root, values=interfaces)
interface_dropdown.pack()
interface_dropdown.bind("<<ComboboxSelected>>", interface_selected)

# Create labels to display interface data
data_label = tk.Label(root, text="Interface Data:")
data_label.pack()
interface_data_label = tk.Label(root, text="")
interface_data_label.pack()

root.mainloop()
