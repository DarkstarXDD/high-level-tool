import threading
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


class RunApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("High Level Tool")
        self.window.geometry("1400x650")

        self.sidebar_frame = sidebar.Sidebar(self.window)
        self.current_frame = currentFrame.CurrentFrame(self.window)

        # Frames
        self.general_frame = generalFrame.GeneralFrame(self.current_frame)
        self.network_frame = networkFrame.NetworkFrame(self.current_frame)
        self.wifi_frame = wifiFrame.WiFiFrame(self.current_frame)
        self.ipscan_frame = ipScannerFrame.IPScannerFrame(self.current_frame)
        self.portscan_frame = portScannerFrame.PortScannerFrame(self.current_frame)
        self.ping_frame = pingFrame.PingFrame(self.current_frame)
        self.traceroute_frame = tracerouteFrame.TracerouteFrame(self.current_frame)
        self.macaddr_frame = macAddressFrame.MacAddressFrame(self.current_frame)

        self.general_frame.lift()

        # Sidebar Buttons
        self.sb_button_general = sb.SidebarButton(
            self.sidebar_frame, "General", self.general_frame
        )
        self.sb_button_netint = sb.SidebarButton(
            self.sidebar_frame, "Network Interfaces", self.network_frame
        )
        self.sb_button_wifi = sb.SidebarButton(
            self.sidebar_frame, "WiFi", self.wifi_frame
        )
        self.sb_button_ip = sb.SidebarButton(
            self.sidebar_frame, "IP Scanner", self.ipscan_frame
        )
        self.sb_button_port = sb.SidebarButton(
            self.sidebar_frame, "Port Scanner", self.portscan_frame
        )
        self.sb_button_ping = sb.SidebarButton(
            self.sidebar_frame, "Ping", self.ping_frame
        )
        self.sb_button_traceroute = sb.SidebarButton(
            self.sidebar_frame, "Traceroute", self.traceroute_frame
        )
        self.sb_button_macaddr = sb.SidebarButton(
            self.sidebar_frame, "MAC Address Lookup", self.macaddr_frame
        )

    def start(self):
        self.window.mainloop()


def start_app():
    app = RunApp()
    app.start()


# Start the Tkinter application in a separate thread
app_thread = threading.Thread(target=start_app)
app_thread.start()
