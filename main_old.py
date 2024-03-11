import getGeoLocationData
import portScanner_old

import tkinter as tk
from tkinter import ttk
import random
import json
import re
import subprocess

BG_COLOR = "#232425"
TEXT_COLOR_100 = "#FFFFFF"
TEXT_COLOR_200 = "#DEE2E6"
TEXT_COLOR_700 = "#ADB5BD"
TEXT_CLR_SIDEBAR = "#C9D1D9"
TEXT_CLR_SIDEBAR_HOVER = "#F3F5F6"
FONT_SIZE_SIDEBAR = 12
FONT_SIZE_LABEL = 10
FONT_SIZE_HOVER_TEXT = 9
FONT_SIZE_HEADING = 12
FONT_LABEL = "Poppins"
FONT_VALUE = "Poppins SemiBold"
SIDEBAR_BUTTON_ACTIVE_CLR = "#313335"
PRIMARY_BLUE = "#4E8FE4"

SIDEBAR_WIDTH = 0.15
CURRENT_FRAME_HEIGHT = 0.95

window = tk.Tk()
window.title("High Level Tool")
window.geometry("1400x650")
window.configure(background=BG_COLOR)
# window.resizable(False, False)


class MainFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        style = ttk.Style()  # Create a Style object
        style.configure("mainframe.TFrame", background="BG_COLOR")

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
            relx=SIDEBAR_WIDTH,
            rely=0,
            relwidth=(1 - SIDEBAR_WIDTH),
            relheight=CURRENT_FRAME_HEIGHT,
        )


class HoverTextBar(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.style = ttk.Style()
        self.style.configure(
            "hovertextbar.TFrame",
            background=BG_COLOR,
        )
        self.configure(style="hovertextbar.TFrame")

        self.style.configure(
            style="hoverlabel.TLabel",
            background=BG_COLOR,
            # borderwidth=10,
            # relief="solid",
            foreground=TEXT_COLOR_200,
            font=(FONT_LABEL, FONT_SIZE_HOVER_TEXT),
        )

        self.place(
            relx=SIDEBAR_WIDTH,
            rely=CURRENT_FRAME_HEIGHT,
            relwidth=(1 - SIDEBAR_WIDTH),
            relheight=(1 - CURRENT_FRAME_HEIGHT),
        )

        self.hover_label = self.create_hover_label()
        # self.set_hover_label("")

    def create_hover_label(self):

        hover_label = ttk.Label(self, text="", style="hoverlabel.TLabel")
        hover_label.pack(expand=True, fill="both", padx=5, pady=4)

        return hover_label

    def set_hover_label(self, label_text):
        self.hover_label.configure(text=label_text)


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
        handle_click_general(event)
        SidebarButton.active_button = self


class GeneralFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        with open("./tooltips.json", "r") as tooltips_file:
            self.tooltips = json.load(tooltips_file)

        self.geolocation_data = getGeoLocationData.GeoLocationData()

        self.general_data = {
            "hostname": "",
            "ipaddress_v4": "",
            "ipaddress_v6": "",
            "mac_address": "",
            "router_ipv4": "",
            "router_ipv6": "",
        }

        # Run ipconfig command
        output_1 = subprocess.check_output(["ipconfig", "/all"]).decode("utf-8")
        # print(output_1)

        # Define regular expression pattern to match IPv4 address
        hostname_pattern = r"Host Name[.\s]+: (.+)"
        ipv4_pattern = r"IPv4 Address[.\s]+: ([\d.]+)"
        ipv6_pattern = r"IPv6 Address[.\s]+: ([\da-fA-F:]+)"

        # Search for Hostname address in the output
        match = re.search(hostname_pattern, output_1)

        if match:
            hostname = match.group(1)
            print(f"Hostname: {hostname}")
            self.general_data["hostname"] = hostname
        else:
            print("Hostname Address not found")
            self.general_data = "-"

        # Search for IPv4 address in the output
        match = re.search(ipv4_pattern, output_1)

        if match:
            ipv4_address = match.group(1)
            print(f"IPv4 Address: {ipv4_address}")
            self.general_data["ipaddress_v4"] = ipv4_address
        else:
            print("IPv4 Address not found")
            self.general_data["ipaddress_v4"] = "-"

        # Search for IPv6 address in the output
        match = re.search(ipv6_pattern, output_1)

        if match:
            ipv6_address = match.group(1)
            print(f"IPv6 Address: {ipv6_address}")
            self.general_data["ipaddress_v6"] = ipv6_address
        else:
            print("IPv6 Address not found")
            self.general_data["ipaddress_v6"] = "-"

        mac_address = self.get_mac_address()
        if mac_address:
            print("MAC Address:", mac_address)
            self.general_data["mac_address"] = mac_address
        else:
            print("Unable to retrieve MAC address.")
            self.general_data["mac_address"] = "-"

        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Get all the data
        # self.general_data = self.get_general_data()
        # self.geolocation_data = self.get_geolocation_data()

        # Styles
        self.style = ttk.Style()
        self.style.configure("general.TFrame", background=BG_COLOR)
        self.configure(style="general.TFrame")

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

        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure(0, weight=1)  # Adjusted weight to 6 (1.2 * 5)
        self.rowconfigure(1, weight=2)  # Adjusted weight to 9 (1.8 * 5)

        computer = self.section_computer(col=0, row=0, colspan=1, rowspan=1)
        router = self.section_router(col=1, row=0, colspan=1, rowspan=1)
        public = self.section_public(col=2, row=0, colspan=1, rowspan=1)
        geo_location = self.section_geolocation(col=0, row=1, colspan=3, rowspan=1)

    def get_mac_address(self):
        try:
            output = subprocess.check_output(
                ["ipconfig", "/all"], universal_newlines=True
            )
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

    # ---------------------------------- Section - Computer ------------------------------------------------
    def section_computer(self, col, row, colspan, rowspan):
        section = self.section_default(col, row, colspan, rowspan)

        section.columnconfigure(0, weight=1)
        section.columnconfigure(1, weight=1)
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
        hostname_name.bind(
            "<Enter>",
            lambda event: hover_text_bar.set_hover_label(self.tooltips["hostname"]),
        )
        hostname_name.bind(
            "<Leave>",
            lambda event: hover_text_bar.set_hover_label(""),
        )

        # IPv4
        ipv4 = self.general_data["ipaddress_v4"]
        ipv4_name = ttk.Label(section, text="IPv4", style="label_name.TLabel")
        ipv4_value = ttk.Label(section, text=ipv4, style="label_value.TLabel")
        ipv4_name.grid(column=0, row=2, sticky="nesw", padx=(10, 0), pady=(0, 5))
        ipv4_value.grid(column=1, row=2, sticky="nesw", padx=(0, 10), pady=(0, 5))
        ipv4_name.bind(
            "<Enter>",
            lambda event: hover_text_bar.set_hover_label(self.tooltips["ipv4"]),
        )
        ipv4_name.bind(
            "<Leave>",
            lambda event: hover_text_bar.set_hover_label(""),
        )

        # IPv6
        ipv6 = self.general_data["ipaddress_v6"]
        ipv6_name = ttk.Label(section, text="IPv6", style="label_name.TLabel")
        ipv6_value = ttk.Label(section, text=ipv6, style="label_value.TLabel")
        ipv6_name.grid(column=0, row=3, sticky="nesw", padx=(10, 0), pady=(0, 5))
        ipv6_value.grid(column=1, row=3, sticky="nesw", padx=(0, 10), pady=(0, 5))
        ipv6_name.bind(
            "<Enter>",
            lambda event: hover_text_bar.set_hover_label(self.tooltips["ipv6"]),
        )
        ipv6_name.bind(
            "<Leave>",
            lambda event: hover_text_bar.set_hover_label(""),
        )

        # MAC Address
        macaddr = self.general_data["mac_address"]
        macaddr_name = ttk.Label(section, text="MAC Address", style="label_name.TLabel")
        macaddr_value = ttk.Label(section, text=macaddr, style="label_value.TLabel")
        macaddr_name.grid(column=0, row=4, sticky="nesw", padx=(10, 0), pady=(0, 5))
        macaddr_value.grid(column=1, row=4, sticky="nesw", padx=(0, 10), pady=(0, 5))
        macaddr_name.bind(
            "<Enter>",
            lambda event: hover_text_bar.set_hover_label(self.tooltips["mac_address"]),
        )
        macaddr_name.bind(
            "<Leave>",
            lambda event: hover_text_bar.set_hover_label(""),
        )

    # -------------------------------------------- Section - Router ------------------------------------------
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
        r_ipv4_name.bind(
            "<Enter>",
            lambda event: hover_text_bar.set_hover_label(self.tooltips["router_ipv4"]),
        )
        r_ipv4_name.bind(
            "<Leave>",
            lambda event: hover_text_bar.set_hover_label(""),
        )

        # Router - IPv6
        r_ipv6 = self.general_data["router_ipv6"]
        r_ipv6_name = ttk.Label(section, text="IPv6", style="label_name.TLabel")
        r_ipv6_value = ttk.Label(section, text=r_ipv6, style="label_value.TLabel")
        r_ipv6_name.grid(column=0, row=2, sticky="nesw", padx=(10, 0), pady=(0, 5))
        r_ipv6_value.grid(column=1, row=2, sticky="nesw", padx=(0, 10), pady=(0, 5))
        r_ipv6_name.bind(
            "<Enter>",
            lambda event: hover_text_bar.set_hover_label(self.tooltips["router_ipv6"]),
        )
        r_ipv6_name.bind(
            "<Leave>",
            lambda event: hover_text_bar.set_hover_label(""),
        )

        # Dummy
        dummy_1 = ttk.Label(section, text="", style="label_name.TLabel")
        dummy_1.grid(column=0, row=3, sticky="nesw", padx=(10, 0), pady=(0, 5))

        # Dummy
        dummy_2 = ttk.Label(section, text="", style="label_name.TLabel")
        dummy_2.grid(column=0, row=4, sticky="nesw", padx=(10, 0), pady=(0, 5))

    # -------------------------------------------- Section - Public --------------------------------------
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
        p_ipv4 = self.geolocation_data.public_ip
        p_ipv4_name = ttk.Label(
            section, text="Your Public IPv4", style="label_name.TLabel"
        )
        p_ipv4_value = ttk.Label(section, text=p_ipv4, style="label_value.TLabel")
        p_ipv4_name.grid(column=0, row=1, sticky="nesw", padx=(10, 0), pady=(0, 5))
        p_ipv4_value.grid(column=1, row=1, sticky="nesw", padx=(0, 10), pady=(0, 5))
        p_ipv4_name.bind(
            "<Enter>",
            lambda event: hover_text_bar.set_hover_label(self.tooltips["public_ipv4"]),
        )
        p_ipv4_name.bind(
            "<Leave>",
            lambda event: hover_text_bar.set_hover_label(""),
        )

        # Dummy
        dummy_1 = ttk.Label(section, text="", style="label_name.TLabel")
        dummy_1.grid(column=0, row=2, sticky="nesw", padx=(10, 0), pady=(0, 5))

        # Dummy
        dummy_2 = ttk.Label(section, text="", style="label_name.TLabel")
        dummy_2.grid(column=0, row=3, sticky="nesw", padx=(10, 0), pady=(0, 5))

        # Dummy
        dummy_3 = ttk.Label(section, text="", style="label_name.TLabel")
        dummy_3.grid(column=0, row=4, sticky="nesw", padx=(10, 0), pady=(0, 5))

    # ------------------------------------------- Section - GeoLocation ------------------------------------------
    def section_geolocation(self, col, row, colspan, rowspan):
        section = self.section_default(col, row, colspan, rowspan)

        section.columnconfigure(0, weight=1)
        section.columnconfigure(1, weight=2)
        section.columnconfigure(2, weight=1)
        section.columnconfigure(3, weight=2)
        section.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1)

        # Logo & Section Heading
        ttk.Label(section, text="IP Geolocation", style="section_heading.TLabel").grid(
            column=0,
            row=0,
            columnspan=2,
            rowspan=1,
            sticky="nesw",
            padx=(10),
            pady=(10, 10),
        )

        continent = self.geolocation_data.continent
        continent_code = self.geolocation_data.continent_code
        continent_name = ttk.Label(section, text="Continent", style="label_name.TLabel")
        continent_value = ttk.Label(
            section, text=f"{continent} ({continent_code})", style="label_value.TLabel"
        )
        continent_name.grid(column=0, row=2, sticky="nesw", padx=(10, 0), pady=(0, 5))
        continent_value.grid(column=1, row=2, sticky="nesw", padx=(0, 10), pady=(0, 5))

        country = self.geolocation_data.country
        country_code = self.geolocation_data.country_code
        country_name = ttk.Label(section, text="Country", style="label_name.TLabel")
        country_value = ttk.Label(
            section, text=f"{country} ({country_code})", style="label_value.TLabel"
        )
        country_name.grid(column=0, row=3, sticky="nesw", padx=(10, 0), pady=(0, 5))
        country_value.grid(column=1, row=3, sticky="nesw", padx=(0, 10), pady=(0, 5))

        region = self.geolocation_data.region_name
        region_name = ttk.Label(section, text="Region", style="label_name.TLabel")
        region_value = ttk.Label(section, text=region, style="label_value.TLabel")
        region_name.grid(column=0, row=4, sticky="nesw", padx=(10, 0), pady=(0, 5))
        region_value.grid(column=1, row=4, sticky="nesw", padx=(0, 10), pady=(0, 5))

        city = self.geolocation_data.city
        city_name = ttk.Label(section, text="City", style="label_name.TLabel")
        city_value = ttk.Label(section, text=city, style="label_value.TLabel")
        city_name.grid(column=0, row=5, sticky="nesw", padx=(10, 0), pady=(0, 5))
        city_value.grid(column=1, row=5, sticky="nesw", padx=(0, 10), pady=(0, 5))

        district = self.geolocation_data.district
        district_name = ttk.Label(section, text="District", style="label_name.TLabel")
        district_value = ttk.Label(section, text=district, style="label_value.TLabel")
        district_name.grid(column=0, row=6, sticky="nesw", padx=(10, 0), pady=(0, 5))
        district_value.grid(column=1, row=6, sticky="nesw", padx=(0, 10), pady=(0, 5))

        zip = self.geolocation_data.zipcode
        zip_name = ttk.Label(section, text="Zip", style="label_name.TLabel")
        zip_value = ttk.Label(section, text=zip, style="label_value.TLabel")
        zip_name.grid(column=0, row=7, sticky="nesw", padx=(10, 0), pady=(0, 5))
        zip_value.grid(column=1, row=7, sticky="nesw", padx=(0, 10), pady=(0, 5))

        lat = self.geolocation_data.lat
        lat_name = ttk.Label(section, text="Latitude", style="label_name.TLabel")
        lat_value = ttk.Label(section, text=lat, style="label_value.TLabel")
        lat_name.grid(column=0, row=8, sticky="nesw", padx=(10, 0), pady=(0, 5))
        lat_value.grid(column=1, row=8, sticky="nesw", padx=(0, 10), pady=(0, 5))

        lon = self.geolocation_data.lon
        lon_name = ttk.Label(section, text="Longitude", style="label_name.TLabel")
        lon_value = ttk.Label(section, text=lon, style="label_value.TLabel")
        lon_name.grid(column=0, row=9, sticky="nesw", padx=(10, 0), pady=(0, 5))
        lon_value.grid(column=1, row=9, sticky="nesw", padx=(0, 10), pady=(0, 5))

        timezone = self.geolocation_data.timezone
        timezone_name = ttk.Label(section, text="Timezone", style="label_name.TLabel")
        timezone_value = ttk.Label(section, text=timezone, style="label_value.TLabel")
        timezone_name.grid(column=0, row=10, sticky="nesw", padx=(10, 0), pady=(0, 5))
        timezone_value.grid(column=1, row=10, sticky="nesw", padx=(0, 10), pady=(0, 5))

        currency = self.geolocation_data.currency
        currency_name = ttk.Label(section, text="Currency", style="label_name.TLabel")
        currency_value = ttk.Label(section, text=currency, style="label_value.TLabel")
        currency_name.grid(column=0, row=11, sticky="nesw", padx=(10, 0), pady=(0, 5))
        currency_value.grid(column=1, row=11, sticky="nesw", padx=(0, 10), pady=(0, 5))

        isp = self.geolocation_data.isp
        isp_name = ttk.Label(section, text="ISP", style="label_name.TLabel")
        isp_value = ttk.Label(section, text=isp, style="label_value.TLabel")
        isp_name.grid(column=2, row=2, sticky="nesw", padx=(10, 0), pady=(0, 5))
        isp_value.grid(column=3, row=2, sticky="nesw", padx=(0, 10), pady=(0, 5))
        isp_name.bind(
            "<Enter>",
            lambda event: hover_text_bar.set_hover_label(self.tooltips["isp"]),
        )
        isp_name.bind(
            "<Leave>",
            lambda event: hover_text_bar.set_hover_label(""),
        )

        org = self.geolocation_data.org
        org_name = ttk.Label(section, text="Organization", style="label_name.TLabel")
        org_value = ttk.Label(section, text=org, style="label_value.TLabel")
        org_name.grid(column=2, row=3, sticky="nesw", padx=(10, 0), pady=(0, 5))
        org_value.grid(column=3, row=3, sticky="nesw", padx=(0, 10), pady=(0, 5))

        asn = self.geolocation_data.asn
        asn_name = ttk.Label(section, text="ASN", style="label_name.TLabel")
        asn_value = ttk.Label(section, text=asn, style="label_value.TLabel")
        asn_name.grid(column=2, row=4, sticky="nesw", padx=(10, 0), pady=(0, 5))
        asn_value.grid(column=3, row=4, sticky="nesw", padx=(0, 10), pady=(0, 5))
        asn_name.bind(
            "<Enter>",
            lambda event: hover_text_bar.set_hover_label(self.tooltips["asn"]),
        )
        asn_name.bind(
            "<Leave>",
            lambda event: hover_text_bar.set_hover_label(""),
        )

        asname = self.geolocation_data.as_name
        asname_name = ttk.Label(section, text="AS Name", style="label_name.TLabel")
        asname_value = ttk.Label(section, text=asname, style="label_value.TLabel")
        asname_name.grid(column=2, row=5, sticky="nesw", padx=(10, 0), pady=(0, 5))
        asname_value.grid(column=3, row=5, sticky="nesw", padx=(0, 10), pady=(0, 5))
        asname_name.bind(
            "<Enter>",
            lambda event: hover_text_bar.set_hover_label(self.tooltips["as_name"]),
        )
        asname_name.bind(
            "<Leave>",
            lambda event: hover_text_bar.set_hover_label(""),
        )

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

    # def get_geolocation_data(self):
    #     geolocation_data = {
    #         "continent": "Asia",
    #         "continentCode": "AS",
    #         "country": "Sri Lanka",
    #         "countryCode": "LK",
    #         "region": "1",
    #         "regionName": "Western Province",
    #         "city": "Battaramulla South",
    #         "district": "",
    #         "zip": "10120",
    #         "lat": 6.8929,
    #         "lon": 79.9187,
    #         "timezone": "Asia/Colombo",
    #         "offset": 19800,
    #         "currency": "LKR",
    #         "isp": "SLTADSL-SLT",
    #         "org": "",
    #         "as": "AS9329 Sri Lanka Telecom Internet",
    #         "asname": "SLTINT-AS-AP",
    #     }

    # return geolocation_data


class NetInterfaces(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.style = ttk.Style()
        self.style.configure("netinterfaces.TFrame", background=BG_COLOR)

        self.configure(style="netinterfaces.TFrame")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)


mainframe = MainFrame(window)
sidebar = Sidebar(mainframe)
currentframe = CurrentFrame(mainframe)
hover_text_bar = HoverTextBar(mainframe)
general_frame = GeneralFrame(currentframe)
net_interfaces = NetInterfaces(currentframe)
port_scanner = portScanner_old.PortScanner(currentframe)

# general_frame.lift()
# print(general_frame)
# print(net_interfaces)


# Sidebar Buttons
btn_general = SidebarButton(sidebar, "General")
btn_network_interfaces = SidebarButton(sidebar, "Network Interfaces")
btn_wifi = SidebarButton(sidebar, "WiFi")
btn_ip_scanner = SidebarButton(sidebar, "IP Scanner")
btn_port_scanner = SidebarButton(sidebar, "Port Scanner")
btn_ping = SidebarButton(sidebar, "Ping")
btn_traceroute = SidebarButton(sidebar, "Traceroute")
btn_mac_lookup = SidebarButton(sidebar, "MAC Address Lookup")


def handle_click_general(event):
    general_frame.lift()


def handle_click_net_interfaces(event):
    net_interfaces.lift()


# btn_general.bind("<Button-1>", handle_click_general)
# btn_network_interfaces.bind("<Button-1>", handle_click_net_interfaces)


window.mainloop()
