import sidebar
import sidebarButton as sb
import currentFrame
import hoverArea
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
import json


SIDEBAR_WIDTH = 0.15
CURRENT_FRAME_HEIGHT = 0.95


class RunApp:
    def __init__(self):

        window = ctk.CTk()
        window.title("High Level Tool")
        window.geometry("1400x650")

        ctk.set_default_color_theme("blue")
        ctk.set_default_color_theme("blue.json")

        sidebar_frame = sidebar.Sidebar(window, SIDEBAR_WIDTH)
        current_frame = currentFrame.CurrentFrame(
            window, SIDEBAR_WIDTH, CURRENT_FRAME_HEIGHT
        )
        hover_area = hoverArea.HoverArea(window, SIDEBAR_WIDTH, CURRENT_FRAME_HEIGHT)

        with open(file="tooltips.json", mode="r") as tooltips_file:
            tooltips = json.load(tooltips_file)

        with open(file="descriptions.json", mode="r") as descriptions_file:
            descriptions = json.load(descriptions_file)

        # Frames
        general_frame = generalFrame.GeneralFrame(current_frame, hover_area, tooltips)
        network_frame = networkFrame.NetworkFrame(current_frame)
        wifi_frame = wifiFrame.WiFiFrame(current_frame)
        ipscan_frame = ipScannerFrame.IPScannerFrame(current_frame)
        portscan_frame = portScannerFrame.PortScannerFrame(
            current_frame, hover_area, tooltips, descriptions
        )
        ping_frame = pingFrame.PingFrame(current_frame)
        traceroute_frame = tracerouteFrame.TracerouteFrame(current_frame)
        macaddr_frame = macAddressFrame.MacAddressFrame(current_frame)

        general_frame.lift()

        # Sidebar Buttons
        sb_button_general = sb.SidebarButton(sidebar_frame, "General", general_frame)
        sb_button_netint = sb.SidebarButton(
            sidebar_frame, "Network Interfaces", network_frame
        )
        sb_button_wifi = sb.SidebarButton(sidebar_frame, "WiFi", wifi_frame)
        sb_button_ip = sb.SidebarButton(sidebar_frame, "IP Scanner", ipscan_frame)
        sb_button_port = sb.SidebarButton(sidebar_frame, "Port Scanner", portscan_frame)
        sb_button_ping = sb.SidebarButton(sidebar_frame, "Ping", ping_frame)
        sb_button_traceroute = sb.SidebarButton(
            sidebar_frame, "Traceroute", traceroute_frame
        )
        sb_button_macaddr = sb.SidebarButton(
            sidebar_frame, "MAC Address Lookup", macaddr_frame
        )

        window.mainloop()


runapp = RunApp()
