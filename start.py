import sidebar
import sidebarButton as sb
import currentFrame
import generalFrame
import networkFrame
import wifiFrame
import ipScannerFrame
import portScannerFrame
import pingFrame
import tracerouteFrame
import macAddressFrame

import getGeoLocationData

import customtkinter as ctk


window = ctk.CTk()
window.title("High Level Tool")
window.geometry("1400x650")

sidebar_frame = sidebar.Sidebar(window)
current_frame = currentFrame.CurrentFrame(window)

# Frames
general_frame = generalFrame.GeneralFrame(current_frame)
network_frame = networkFrame.NetworkFrame(current_frame)
wifi_frame = wifiFrame.WiFiFrame(current_frame)
ipscan_frame = ipScannerFrame.IPScannerFrame(current_frame)
portscan_frame = portScannerFrame.PortScannerFrame(current_frame)
ping_frame = pingFrame.PingFrame(current_frame)
traceroute_frame = tracerouteFrame.TracerouteFrame(current_frame)
macaddr_frame = macAddressFrame.MacAddressFrame(current_frame)

general_frame.lift()


# Sidebar Buttons
sb_button_general = sb.SidebarButton(sidebar_frame, "General", general_frame)
sb_button_netint = sb.SidebarButton(sidebar_frame, "Network Interfaces", network_frame)
sb_button_wifi = sb.SidebarButton(sidebar_frame, "WiFi", wifi_frame)
sb_button_ip = sb.SidebarButton(sidebar_frame, "IP Scanner", ipscan_frame)
sb_button_port = sb.SidebarButton(sidebar_frame, "Port Scanner", portscan_frame)
sb_button_ping = sb.SidebarButton(sidebar_frame, "Ping", ping_frame)
sb_button_traceroute = sb.SidebarButton(sidebar_frame, "Traceroute", traceroute_frame)
sb_button_macaddr = sb.SidebarButton(sidebar_frame, "MAC Address Lookup", macaddr_frame)


window.mainloop()
