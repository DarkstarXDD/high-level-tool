import os
import sys
import json

import customtkinter as ctk

import sidebar
import sidebarButton as sb
import currentFrame
import hoverArea
import generalFrame
import networkFrame
import usageMonitorFrame
import pingSweepFrame
import portScannerFrame
import pingFrame
import tracerouteFrame
import macLookupFrame


SIDEBAR_WIDTH = 0.15
CURRENT_FRAME_HEIGHT = 0.95


class RunApp:
    def __init__(self):

        window = ctk.CTk()
        window.title("High Level Tool")
        window.geometry("1400x650")

        ctk.set_default_color_theme(self.resource_path("./data/blue.json"))

        sidebar_frame = sidebar.Sidebar(window, SIDEBAR_WIDTH)
        current_frame = currentFrame.CurrentFrame(
            window, SIDEBAR_WIDTH, CURRENT_FRAME_HEIGHT
        )
        hover_area = hoverArea.HoverArea(window, SIDEBAR_WIDTH, CURRENT_FRAME_HEIGHT)

        with open(
            file=self.resource_path("./data/tooltips.json"),
            encoding="utf-8",
            mode="r",
        ) as tooltips_file:
            tooltips = json.load(tooltips_file)

        with open(
            file=self.resource_path("./data/descriptions.json"),
            encoding="utf-8",
            mode="r",
        ) as descriptions_file:
            descriptions = json.load(descriptions_file)

        # Frames
        general_frame = generalFrame.GeneralFrame(current_frame, hover_area, tooltips)
        network_frame = networkFrame.NetworkFrame(current_frame)
        usage_frame = usageMonitorFrame.UsageMonitorFrame(
            current_frame, hover_area, tooltips
        )
        pingsweep_frame = pingSweepFrame.PingSweepFrame(
            current_frame, hover_area, tooltips, descriptions
        )
        portscan_frame = portScannerFrame.PortScannerFrame(
            current_frame, hover_area, tooltips, descriptions
        )
        ping_frame = pingFrame.PingFrame(
            current_frame, hover_area, tooltips, descriptions
        )
        traceroute_frame = tracerouteFrame.TracerouteFrame(
            current_frame, hover_area, tooltips, descriptions
        )
        mac_lookup_frame = macLookupFrame.MacLookupFrame(
            current_frame, hover_area, tooltips, descriptions
        )

        general_frame.lift()

        # Sidebar Buttons
        sb.SidebarButton(sidebar_frame, "General", general_frame)
        sb.SidebarButton(sidebar_frame, "Network Interfaces", network_frame)
        sb.SidebarButton(sidebar_frame, "Data Usage Monitor", usage_frame)
        sb.SidebarButton(sidebar_frame, "Ping Sweep", pingsweep_frame)
        sb.SidebarButton(sidebar_frame, "Port Scanner", portscan_frame)
        sb.SidebarButton(sidebar_frame, "Ping", ping_frame)
        sb.SidebarButton(sidebar_frame, "Traceroute", traceroute_frame)
        sb.SidebarButton(sidebar_frame, "MAC Address Lookup", mac_lookup_frame)

        window.mainloop()

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS2
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


runapp = RunApp()
