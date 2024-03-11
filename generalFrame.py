import customtkinter as ctk


class GeneralFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(corner_radius=0, fg_color="#242424")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure(0, weight=1, uniform="a")
        self.rowconfigure(1, weight=2, uniform="a")

        # Create 4 Frames for the Sections
        frame_pc = ctk.CTkFrame(self)
        frame_router = ctk.CTkFrame(self)
        frame_public = ctk.CTkFrame(self)
        frame_geoip = ctk.CTkFrame(self)

        # Place the 4 Frames (Sections)
        frame_pc.grid(column=0, row=0, sticky="nesw", padx=(10, 5), pady=(10, 5))
        frame_router.grid(column=1, row=0, sticky="nesw", padx=5, pady=(10, 5))
        frame_public.grid(column=2, row=0, sticky="nesw", padx=(5, 10), pady=(10, 5))
        frame_geoip.grid(row=1, columnspan=3, sticky="nesw", padx=(10), pady=(5, 10))

        # ------------------------------------------------------------------------
        # ---------------------------------- PC ----------------------------------
        # ------------------------------------------------------------------------
        frame_pc.columnconfigure(0, weight=1)
        frame_pc.columnconfigure(1, weight=1)
        frame_pc.rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Logo & Section Heading
        label_pc = ctk.CTkLabel(frame_pc, text="This PC")
        label_pc.grid(columnspan=2, rowspan=1, sticky="nesw", padx=(10), pady=(10, 10))

        # Hostname
        # hostname = self.general_data["hostname"]
        hostname_name = ctk.CTkLabel(frame_pc, text="Hostname")
        hostname_name.grid(column=0, row=1, sticky="nesw", padx=(10, 0), pady=(0, 5))

        hostname_value = ctk.CTkLabel(frame_pc, text="Graveyard")
        hostname_value.grid(column=1, row=1, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # IPv4
        # ipv4 = self.general_data["ipaddress_v4"]
        ipv4_name = ctk.CTkLabel(frame_pc, text="IPv4")
        ipv4_name.grid(column=0, row=2, sticky="nesw", padx=(10, 0), pady=(0, 5))

        ipv4_value = ctk.CTkLabel(frame_pc, text="192.168.1.50")
        ipv4_value.grid(column=1, row=2, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # IPv6
        # ipv6 = self.general_data["ipaddress_v6"]
        ipv6_name = ctk.CTkLabel(frame_pc, text="IPv6")
        ipv6_value = ctk.CTkLabel(frame_pc, text="fe80")
        ipv6_name.grid(column=0, row=3, sticky="nesw", padx=(10, 0), pady=(0, 5))
        ipv6_value.grid(column=1, row=3, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # MAC Address
        # macaddr = self.general_data["mac_address"]
        macaddr_name = ctk.CTkLabel(frame_pc, text="MAC Address")
        macaddr_value = ctk.CTkLabel(frame_pc, text="B4:34:C3:E8")
        macaddr_name.grid(column=0, row=4, sticky="nesw", padx=(10, 0), pady=(0, 5))
        macaddr_value.grid(column=1, row=4, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # ------------------------------------------------------------------------
        # -------------------------------- Router --------------------------------
        # ------------------------------------------------------------------------
        frame_router.columnconfigure(0, weight=1)
        frame_router.columnconfigure(1, weight=1)
        frame_router.rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Logo & Section Heading
        label_router = ctk.CTkLabel(frame_router, text="Gateway/Router")
        label_router.grid(columnspan=2, rowspan=1, sticky="nesw", padx=(10), pady=(10))

        # Router - IPv4
        # r_ipv4 = self.general_data["router_ipv4"]
        r_ipv4_name = ctk.CTkLabel(frame_router, text="IPv4")
        r_ipv4_name.grid(column=0, row=1, sticky="nesw", padx=(10, 0), pady=(0, 5))

        r_ipv4_value = ctk.CTkLabel(frame_router, text="192.168.1.1")
        r_ipv4_value.grid(column=1, row=1, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # Router - IPv6
        # r_ipv6 = self.general_data["router_ipv6"]
        r_ipv6_name = ctk.CTkLabel(frame_router, text="IPv6")
        r_ipv6_value = ctk.CTkLabel(frame_router, text="fe:800")
        r_ipv6_name.grid(column=0, row=2, sticky="nesw", padx=(10, 0), pady=(0, 5))
        r_ipv6_value.grid(column=1, row=2, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # Dummy
        dummy_1 = ctk.CTkLabel(frame_router, text="")
        dummy_1.grid(column=0, row=3, sticky="nesw", padx=(10, 0), pady=(0, 5))

        # Dummy
        dummy_2 = ctk.CTkLabel(frame_router, text="")
        dummy_2.grid(column=0, row=4, sticky="nesw", padx=(10, 0), pady=(0, 5))

        # ------------------------------------------------------------------------
        # -------------------------------- Public --------------------------------
        # ------------------------------------------------------------------------
        frame_public.columnconfigure(0, weight=1)
        frame_public.columnconfigure(1, weight=1)
        frame_public.rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Logo & Section Heading
        label_public = ctk.CTkLabel(frame_public, text="Public")
        label_public.grid(columnspan=2, rowspan=1, sticky="nesw", padx=(10), pady=(10))

        # Public IPv4
        # p_ipv4 = self.geolocation_data.public_ip
        p_ipv4_name = ctk.CTkLabel(frame_public, text="Your Public IPv4")
        p_ipv4_value = ctk.CTkLabel(frame_public, text="112.119.24.31")
        p_ipv4_name.grid(column=0, row=1, sticky="nesw", padx=(10, 0), pady=(0, 5))
        p_ipv4_value.grid(column=1, row=1, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # Dummy
        dummy_1 = ctk.CTkLabel(frame_public, text="")
        dummy_1.grid(column=0, row=2, sticky="nesw", padx=(10, 0), pady=(0, 5))

        # Dummy
        dummy_2 = ctk.CTkLabel(frame_public, text="")
        dummy_2.grid(column=0, row=3, sticky="nesw", padx=(10, 0), pady=(0, 5))

        # Dummy
        dummy_3 = ctk.CTkLabel(frame_public, text="")
        dummy_3.grid(column=0, row=4, sticky="nesw", padx=(10, 0), pady=(0, 5))

        # ------------------------------------------------------------------------
        # -------------------------------- GeoIP --------------------------------
        # ------------------------------------------------------------------------
        frame_geoip.columnconfigure(0, weight=1)
        frame_geoip.columnconfigure(1, weight=2)
        frame_geoip.columnconfigure(2, weight=1)
        frame_geoip.columnconfigure(3, weight=2)
        frame_geoip.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1)

        # Logo & Section Heading
        label_geoip = ctk.CTkLabel(frame_geoip, text="IP Geolocation")
        label_geoip.grid(columnspan=2, rowspan=1, sticky="nesw", padx=(10), pady=(10))

        # Continent & Continent Code
        # continent = self.geolocation_data.continent
        continent = "Asia"
        # continent_code = self.geolocation_data.continent_code
        continent_code = "AS"
        continent_name = ctk.CTkLabel(frame_geoip, text="Continent")
        continent_value = ctk.CTkLabel(
            frame_geoip, text=f"{continent} ({continent_code})"
        )
        continent_name.grid(column=0, row=2, sticky="nesw", padx=(10, 0), pady=(0, 5))
        continent_value.grid(column=1, row=2, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # country = self.geolocation_data.country
        country = "Sri Lanka"
        # country_code = self.geolocation_data.country_code
        country_code = "LK"
        country_name = ctk.CTkLabel(frame_geoip, text="Country")
        country_value = ctk.CTkLabel(frame_geoip, text=f"{country} ({country_code})")
        country_name.grid(column=0, row=3, sticky="nesw", padx=(10, 0), pady=(0, 5))
        country_value.grid(column=1, row=3, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # region = self.geolocation_data.region_name
        region = "Western Province"
        region_name = ctk.CTkLabel(frame_geoip, text="Region")
        region_value = ctk.CTkLabel(frame_geoip, text=region)
        region_name.grid(column=0, row=4, sticky="nesw", padx=(10, 0), pady=(0, 5))
        region_value.grid(column=1, row=4, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # city = self.geolocation_data.city
        city = "Battaramulla South"
        city_name = ctk.CTkLabel(frame_geoip, text="City")
        city_value = ctk.CTkLabel(frame_geoip, text=city)
        city_name.grid(column=0, row=5, sticky="nesw", padx=(10, 0), pady=(0, 5))
        city_value.grid(column=1, row=5, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # district = self.geolocation_data.district
        district = "-"
        district_name = ctk.CTkLabel(frame_geoip, text="District")
        district_value = ctk.CTkLabel(frame_geoip, text=district)
        district_name.grid(column=0, row=6, sticky="nesw", padx=(10, 0), pady=(0, 5))
        district_value.grid(column=1, row=6, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # zipcode = self.geolocation_data.zipcode
        zipcode = "10120"
        zip_name = ctk.CTkLabel(frame_geoip, text="Zip")
        zip_value = ctk.CTkLabel(frame_geoip, text=zipcode)
        zip_name.grid(column=0, row=7, sticky="nesw", padx=(10, 0), pady=(0, 5))
        zip_value.grid(column=1, row=7, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # lat = self.geolocation_data.lat
        lat = "80.6554"
        lat_name = ctk.CTkLabel(frame_geoip, text="Latitude")
        lat_value = ctk.CTkLabel(frame_geoip, text=lat)
        lat_name.grid(column=0, row=8, sticky="nesw", padx=(10, 0), pady=(0, 5))
        lat_value.grid(column=1, row=8, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # lon = self.geolocation_data.lon
        lon = "6.98"
        lon_name = ctk.CTkLabel(frame_geoip, text="Longitude")
        lon_value = ctk.CTkLabel(frame_geoip, text=lon)
        lon_name.grid(column=0, row=9, sticky="nesw", padx=(10, 0), pady=(0, 5))
        lon_value.grid(column=1, row=9, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # timezone = self.geolocation_data.timezone
        timezone = "Asia/AS"
        timezone_name = ctk.CTkLabel(frame_geoip, text="Timezone")
        timezone_value = ctk.CTkLabel(frame_geoip, text=timezone)
        timezone_name.grid(column=0, row=10, sticky="nesw", padx=(10, 0), pady=(0, 5))
        timezone_value.grid(column=1, row=10, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # currency = self.geolocation_data.currency
        currency = "LK"
        currency_name = ctk.CTkLabel(frame_geoip, text="Currency")
        currency_value = ctk.CTkLabel(frame_geoip, text=currency)
        currency_name.grid(column=0, row=11, sticky="nesw", padx=(10, 0), pady=(0, 5))
        currency_value.grid(column=1, row=11, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # isp = self.geolocation_data.isp
        isp = "SLT - Sri Lanka Telecom"
        isp_name = ctk.CTkLabel(frame_geoip, text="ISP")
        isp_value = ctk.CTkLabel(frame_geoip, text=isp)
        isp_name.grid(column=2, row=2, sticky="nesw", padx=(10, 0), pady=(0, 5))
        isp_value.grid(column=3, row=2, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # org = self.geolocation_data.org
        org = "-"
        org_name = ctk.CTkLabel(frame_geoip, text="Organization")
        org_value = ctk.CTkLabel(frame_geoip, text=org)
        org_name.grid(column=2, row=3, sticky="nesw", padx=(10, 0), pady=(0, 5))
        org_value.grid(column=3, row=3, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # asn = self.geolocation_data.asn
        asn = "SLT123"
        asn_name = ctk.CTkLabel(frame_geoip, text="ASN")
        asn_value = ctk.CTkLabel(frame_geoip, text=asn)
        asn_name.grid(column=2, row=4, sticky="nesw", padx=(10, 0), pady=(0, 5))
        asn_value.grid(column=3, row=4, sticky="nesw", padx=(0, 10), pady=(0, 5))

        # asname = self.geolocation_data.as_name
        asname = "SLT"
        asname_name = ctk.CTkLabel(frame_geoip, text="AS Name")
        asname_value = ctk.CTkLabel(frame_geoip, text=asname)
        asname_name.grid(column=2, row=5, sticky="nesw", padx=(10, 0), pady=(0, 5))
        asname_value.grid(column=3, row=5, sticky="nesw", padx=(0, 10), pady=(0, 5))
