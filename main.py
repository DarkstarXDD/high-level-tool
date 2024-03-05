import tkinter as tk
from tkinter import ttk
import random

window = tk.Tk()
window.title("High Level Tool")
window.geometry("1300x650")
# window.resizable(False, False)

BG_COLOR = "#232425"
TEXT_COLOR_100 = "#FFFFFF"
TEXT_COLOR_200 = "#DEE2E6"
TEXT_COLOR_700 = "#ADB5BD"
TEXT_CLR_SIDEBAR = "#C9D1D9"
TEXT_CLR_SIDEBAR_HOVER = "#F3F5F6"
FONT_SIZE_SIDEBAR = 12
FONT_SIZE_LABEL = 10
FONT_SIZE_HEADING = 12
FONT_LABEL = "Poppins"
FONT_VALUE = "Poppins SemiBold"
SIDEBAR_BUTTON_ACTIVE_CLR = "#313335"
PRIMARY_BLUE = "#4E8FE4"

SIDEBAR_WIDTH = 0.2


class MainFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        style = ttk.Style()  # Create a Style object
        style.configure("mainframe.TFrame", background=BG_COLOR)

        self.configure(style="mainframe.TFrame")

        self.place(relx=0, rely=0, relheight=1, relwidth=1)


class Sidebar(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        style = ttk.Style()
        style.configure(
            "sidebar.TFrame",
            background=BG_COLOR,
            borderwidth=40,
            relief="solid",
            foregound="green",
        )

        self.configure(style="sidebar.TFrame")

        self.place(relx=0, rely=0, relwidth=SIDEBAR_WIDTH, relheight=1)


class CurrentFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        style = ttk.Style()
        style.configure(
            "currentframe.TFrame",
            background=BG_COLOR,
            borderwidth=40,
            relief="solid",
            foregound="green",
        )

        self.configure(style="currentframe.TFrame")

        self.place(
            relx=SIDEBAR_WIDTH, rely=0, relwidth=(1 - SIDEBAR_WIDTH), relheight=1
        )


class SidebarButton(ttk.Label):

    active_button = None

    def __init__(self, parent, btn_text):
        super().__init__(parent)

        self.is_clicked = False

        self.instance_style_name = f"sidebarbutton_{id(self)}.TLabel"  # the id() function returns the identity of an object, which is a unique integer representing the object's identity
        self.style = ttk.Style()
        self.style.configure(
            self.instance_style_name,
            background=BG_COLOR,
            foreground=TEXT_CLR_SIDEBAR,
            font=("Poppins", FONT_SIZE_SIDEBAR),
            justify="center",
        )

        self.configure(text=btn_text, style=self.instance_style_name)
        self.pack(expand=True, fill="both", padx=1)

        self.bind("<Enter>", self.handle_enter)
        self.bind("<Leave>", self.handle_leave)
        self.bind("<Button-1>", self.handle_click)  # <ButtonRelease-1>

    def handle_enter(self, event):
        if SidebarButton.active_button != self:
            self.style.configure(
                self.instance_style_name,
                background=SIDEBAR_BUTTON_ACTIVE_CLR,
                foreground=TEXT_CLR_SIDEBAR_HOVER,
                # font=("Poppins SemiBold", FONT_SIZE_SIDEBAR),
            )

    def handle_leave(self, event):
        if SidebarButton.active_button != self:
            self.style.configure(
                self.instance_style_name,
                background=BG_COLOR,
                foreground=TEXT_CLR_SIDEBAR,
                # font=("Poppins", FONT_SIZE_SIDEBAR),
            )

    def handle_click(self, event):
        if SidebarButton.active_button is not None:
            SidebarButton.active_button.style.configure(
                SidebarButton.active_button.instance_style_name,
                background=BG_COLOR,
                foreground=TEXT_CLR_SIDEBAR,
                # font=("Poppins", FONT_SIZE_SIDEBAR),
            )

        self.style.configure(
            self.instance_style_name,
            background=SIDEBAR_BUTTON_ACTIVE_CLR,
            foreground=PRIMARY_BLUE,
            # font=("Poppins SemiBold", FONT_SIZE_SIDEBAR),
        )

        SidebarButton.active_button = self


class GeneralFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Get all the data
        self.general_data = self.get_general_data()

        self.style = ttk.Style()
        self.style.configure("general.TFrame", background=BG_COLOR)

        self.style.configure(
            "section.TFrame", background=BG_COLOR, borderwidth=2, relief="solid"
        )

        self.style.configure(
            "label_name.TLabel",
            background=BG_COLOR,
            foreground=TEXT_COLOR_200,
            font=(FONT_LABEL, FONT_SIZE_LABEL),
        )

        self.style.configure(
            "label_value.TLabel",
            background=BG_COLOR,
            foreground=TEXT_COLOR_100,
            font=(FONT_VALUE, FONT_SIZE_LABEL),
        )

        self.style.configure(
            "section_heading.TLabel",
            background=BG_COLOR,
            foreground=TEXT_COLOR_700,
            font=(FONT_VALUE, FONT_SIZE_HEADING),
        )

        self.configure(style="general.TFrame")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure(0, weight=1)  # Adjusted weight to 6 (1.2 * 5)
        self.rowconfigure(1, weight=12)  # Adjusted weight to 9 (1.8 * 5)

        computer = self.section_computer(col=0, row=0, colspan=1, rowspan=1)
        router = self.section_router(col=1, row=0, colspan=1, rowspan=1)
        public = self.section_public(col=2, row=0, colspan=1, rowspan=1)
        geo_location = self.section_geolocation(col=0, row=1, colspan=3, rowspan=1)

    # Section - Computer
    def section_computer(self, col, row, colspan, rowspan):
        section = self.section_default(col, row, colspan, rowspan)

        section.columnconfigure(0, weight=1)
        section.columnconfigure(1, weight=6)
        section.rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Logo & Section Heading
        ttk.Label(section, text="This Computer", style="section_heading.TLabel").grid(
            column=0,
            row=0,
            columnspan=2,
            rowspan=1,
            sticky="nesw",
            padx=(10),
            pady=(10, 10),
        )

        # Hostname
        hostname = self.general_data["hostname"]
        hostname_name = ttk.Label(section, text="Hostname", style="label_name.TLabel")
        hostname_value = ttk.Label(section, text=hostname, style="label_value.TLabel")
        hostname_name.grid(column=0, row=1, sticky="nesw", padx=(10, 0), pady=(0, 5))
        hostname_value.grid(column=1, row=1, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # IPv4
        ipv4 = self.general_data["ipaddress_v4"]
        ipv4_name = ttk.Label(section, text="IPv4", style="label_name.TLabel")
        ipv4_value = ttk.Label(section, text=ipv4, style="label_value.TLabel")
        ipv4_name.grid(column=0, row=2, sticky="nesw", padx=(10, 0), pady=(0, 5))
        ipv4_value.grid(column=1, row=2, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # IPv6
        ipv6 = self.general_data["ipaddress_v6"]
        ipv6_name = ttk.Label(section, text="IPv6", style="label_name.TLabel")
        ipv6_value = ttk.Label(section, text=ipv6, style="label_value.TLabel")
        ipv6_name.grid(column=0, row=3, sticky="nesw", padx=(10, 0), pady=(0, 5))
        ipv6_value.grid(column=1, row=3, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # MAC Address
        macaddr = self.general_data["mac_address"]
        macaddr_name = ttk.Label(section, text="MAC Address", style="label_name.TLabel")
        macaddr_value = ttk.Label(section, text=macaddr, style="label_value.TLabel")
        macaddr_name.grid(column=0, row=4, sticky="nesw", padx=(10, 0), pady=(0, 5))
        macaddr_value.grid(column=1, row=4, sticky="nesw", padx=(0, 10), pady=(0, 5))

    # Section - Router
    def section_router(self, col, row, colspan, rowspan):
        section = self.section_default(col, row, colspan, rowspan)

        section.columnconfigure(0, weight=1)
        section.columnconfigure(1, weight=6)
        section.rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Logo & Section Heading
        ttk.Label(section, text="Gateway/Router", style="section_heading.TLabel").grid(
            column=0,
            row=0,
            columnspan=2,
            rowspan=1,
            sticky="nesw",
            padx=(10),
            pady=(10, 10),
        )

        # Router - IPv4
        r_ipv4 = self.general_data["router_ipv4"]
        r_ipv4_name = ttk.Label(section, text="IPv4", style="label_name.TLabel")
        r_ipv4_value = ttk.Label(section, text=r_ipv4, style="label_value.TLabel")
        r_ipv4_name.grid(column=0, row=1, sticky="nesw", padx=(10, 0), pady=(0, 5))
        r_ipv4_value.grid(column=1, row=1, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # Router - IPv6
        r_ipv6 = self.general_data["router_ipv6"]
        r_ipv6_name = ttk.Label(section, text="IPv6", style="label_name.TLabel")
        r_ipv6_value = ttk.Label(section, text=r_ipv6, style="label_value.TLabel")
        r_ipv6_name.grid(column=0, row=2, sticky="nesw", padx=(10, 0), pady=(0, 5))
        r_ipv6_value.grid(column=1, row=2, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # Dummy
        dummy_1 = ttk.Label(section, text="", style="label_name.TLabel")
        dummy_1.grid(column=0, row=3, sticky="nesw", padx=(10, 0), pady=(0, 5))

        # Dummy
        dummy_2 = ttk.Label(section, text="", style="label_name.TLabel")
        dummy_2.grid(column=0, row=4, sticky="nesw", padx=(10, 0), pady=(0, 5))

    # Section - Public
    def section_public(self, col, row, colspan, rowspan):
        section = self.section_default(col, row, colspan, rowspan)

        section.columnconfigure(0, weight=1)
        section.columnconfigure(1, weight=6)
        section.rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Logo & Section Heading
        ttk.Label(section, text="Public", style="section_heading.TLabel").grid(
            column=0,
            row=0,
            columnspan=2,
            rowspan=1,
            sticky="nesw",
            padx=(10),
            pady=(10, 10),
        )

        # Public IPv4
        p_ipv4 = self.get_public_ipv4()
        p_ipv4_name = ttk.Label(
            section, text="Your Public IPv4", style="label_name.TLabel"
        )
        p_ipv4_value = ttk.Label(section, text=p_ipv4, style="label_value.TLabel")
        p_ipv4_name.grid(column=0, row=1, sticky="nesw", padx=(10, 0), pady=(0, 5))
        p_ipv4_value.grid(column=1, row=1, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # Dummy
        dummy_1 = ttk.Label(section, text="", style="label_name.TLabel")
        dummy_1.grid(column=0, row=2, sticky="nesw", padx=(10, 0), pady=(0, 5))

        # Dummy
        dummy_2 = ttk.Label(section, text="", style="label_name.TLabel")
        dummy_2.grid(column=0, row=3, sticky="nesw", padx=(10, 0), pady=(0, 5))

        # Dummy
        dummy_3 = ttk.Label(section, text="", style="label_name.TLabel")
        dummy_3.grid(column=0, row=4, sticky="nesw", padx=(10, 0), pady=(0, 5))

    # Section - GeoLocation
    def section_geolocation(self, col, row, colspan, rowspan):
        self.section_default(col, row, colspan, rowspan)

    # Default Layout for All the Sections
    def section_default(self, col, row, colspan, rowspan):

        section_frame = ttk.Frame(self, style="section.TFrame")
        section_frame.grid(
            column=col,
            row=row,
            columnspan=colspan,
            rowspan=rowspan,
            sticky="nesw",
            padx=5,
            pady=5,
        )

        return section_frame

    def get_general_data(self):
        general_data = {
            "hostname": "desktop-dc",
            "ipaddress_v4": "192.168.1.4",
            "ipaddress_v6": "2402::2424dd",
            "mac_address": "B4:2E:99:A4:9B:08",
            "router_ipv4": "192.168.1.1",
            "router_ipv6": "fe80::a",
        }

        return general_data

    def get_public_ipv4(self):
        public_ip_v4 = "112.134.1.39"
        return public_ip_v4

    def get_geolocation_data(self):
        geolocation_data = {
            "country": "sri lanka",
            "country_code": "lk",
            "zip": "10120",
        }

        return geolocation_data


mainframe = MainFrame(window)
sidebar = Sidebar(mainframe)
currentframe = CurrentFrame(mainframe)
general_frame = GeneralFrame(currentframe)

# Sidebar Buttons
btn_general = SidebarButton(sidebar, "General")
btn_network_interface = SidebarButton(sidebar, "Network Interfaces")
btn_wifi = SidebarButton(sidebar, "WiFi")
btn_ip_scanner = SidebarButton(sidebar, "IP Scanner")
btn_port_scanner = SidebarButton(sidebar, "Port Scanner")
btn_ping = SidebarButton(sidebar, "Ping")
btn_traceroute = SidebarButton(sidebar, "Traceroute")
btn_mac_lookup = SidebarButton(sidebar, "MAC Address Lookup")

window.mainloop()
