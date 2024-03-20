import customtkinter as ctk
import socket
import getGeneralData

TEXT_CLR_700 = "#2586D0"
LP = 15  # PadX - Left


class GeneralFrame(ctk.CTkFrame):
    def __init__(self, parent, hover, tooltips):
        super().__init__(parent)

        self.general_data = getGeneralData.GeneralData()

        self.poppins_400 = ctk.CTkFont(family="Poppins SemiBold", size=18)
        self.poppins_300 = ctk.CTkFont(family="Poppins Medium", size=14)
        self.poppins_200 = ctk.CTkFont(family="Poppins", size=14)

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
        label_pc = ctk.CTkLabel(frame_pc, text="This PC", anchor="w")
        label_pc.configure(font=self.poppins_400, text_color=TEXT_CLR_700)
        label_pc.grid(columnspan=2, rowspan=1, sticky="nesw", padx=(LP), pady=(10))

        # Hostname
        hostname = self.general_data.hostname
        hostname_name = ctk.CTkLabel(frame_pc, text="Hostname", anchor="w")
        hostname_name.configure(font=self.poppins_200)
        hostname_name.grid(column=0, row=1, sticky="nesw", padx=(LP, 0), pady=(0, 5))

        hostname_value = ctk.CTkLabel(frame_pc, text=hostname, anchor="w")
        hostname_value.grid(column=1, row=1, sticky="nesw", padx=(0, 10), pady=(0, 5))
        hostname_value.configure(font=self.poppins_300)

        hostname_name.bind("<Enter>", lambda event: hover.display(tooltips["hostname"]))
        hostname_name.bind("<Leave>", lambda event: hover.display(""))

        # IPv4
        ipv4 = self.general_data.ipv4_address
        ipv4_name = ctk.CTkLabel(frame_pc, text="IPv4", anchor="w")
        ipv4_name.grid(column=0, row=2, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        ipv4_name.configure(font=self.poppins_200)

        ipv4_value = ctk.CTkLabel(frame_pc, text=ipv4, anchor="w")
        ipv4_value.grid(column=1, row=2, sticky="nesw", padx=(0, 10), pady=(0, 5))
        ipv4_value.configure(font=self.poppins_300)

        ipv4_name.bind("<Enter>", lambda event: hover.display(tooltips["ipv4"]))
        ipv4_name.bind("<Leave>", lambda event: hover.display(""))

        # IPv6
        ipv6 = self.general_data.ipv6_address
        ipv6_name = ctk.CTkLabel(frame_pc, text="IPv6", anchor="w")
        ipv6_name.grid(column=0, row=3, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        ipv6_name.configure(font=self.poppins_200)

        ipv6_value = ctk.CTkLabel(frame_pc, text=ipv6, anchor="w")
        ipv6_value.grid(column=1, row=3, sticky="nesw", padx=(0, 10), pady=(0, 5))
        ipv6_value.configure(font=self.poppins_300)

        ipv6_name.bind("<Enter>", lambda event: hover.display(tooltips["ipv6"]))
        ipv6_name.bind("<Leave>", lambda event: hover.display(""))

        # MAC Address
        macaddr = self.general_data.mac_address
        mac_name = ctk.CTkLabel(frame_pc, text="MAC Address", anchor="w")
        mac_name.grid(column=0, row=4, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        mac_name.configure(font=self.poppins_200)

        mac_value = ctk.CTkLabel(frame_pc, text=macaddr, anchor="w")
        mac_value.grid(column=1, row=4, sticky="nesw", padx=(0, 10), pady=(0, 5))
        mac_value.configure(font=self.poppins_300)

        mac_name.bind("<Enter>", lambda event: hover.display(tooltips["mac_address"]))
        mac_name.bind("<Leave>", lambda event: hover.display(""))

        # ------------------------------------------------------------------------
        # -------------------------------- Router --------------------------------
        # ------------------------------------------------------------------------
        frame_router.columnconfigure(0, weight=1)
        frame_router.columnconfigure(1, weight=1)
        frame_router.rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Logo & Section Heading
        label_router = ctk.CTkLabel(frame_router, text="Gateway/Router", anchor="w")
        label_router.configure(font=self.poppins_400, text_color=TEXT_CLR_700)
        label_router.grid(columnspan=2, rowspan=1, sticky="nesw", padx=(LP), pady=(10))

        # Router - IPv4
        # r_ipv4 = self.general_data["router_ipv4"]
        r_ipv4_name = ctk.CTkLabel(frame_router, text="IPv4", anchor="w")
        r_ipv4_name.grid(column=0, row=1, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        r_ipv4_name.configure(font=self.poppins_200)

        r_ipv4_value = ctk.CTkLabel(frame_router, text="192.168.1.1", anchor="w")
        r_ipv4_value.grid(column=1, row=1, sticky="nesw", padx=(0, 10), pady=(0, 5))
        r_ipv4_value.configure(font=self.poppins_300)

        r_ipv4_name.bind("<Enter>", lambda event: hover.display(tooltips["r_ipv4"]))
        r_ipv4_name.bind("<Leave>", lambda event: hover.display(""))

        # Router - IPv6
        # r_ipv6 = self.general_data["router_ipv6"]
        r_ipv6_name = ctk.CTkLabel(frame_router, text="IPv6", anchor="w")
        r_ipv6_name.grid(column=0, row=2, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        r_ipv6_name.configure(font=self.poppins_200)

        r_ipv6_value = ctk.CTkLabel(frame_router, text="fe:800", anchor="w")
        r_ipv6_value.grid(column=1, row=2, sticky="nesw", padx=(0, 10), pady=(0, 5))
        r_ipv6_value.configure(font=self.poppins_300)

        r_ipv6_name.bind("<Enter>", lambda event: hover.display(tooltips["r_ipv6"]))
        r_ipv6_name.bind("<Leave>", lambda event: hover.display(""))

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
        label_public = ctk.CTkLabel(frame_public, text="Public", anchor="w")
        label_public.configure(font=self.poppins_400, text_color=TEXT_CLR_700)
        label_public.grid(columnspan=2, rowspan=1, sticky="nesw", padx=(LP), pady=(10))

        # Public IPv4
        # p_ipv4 = self.geolocation_data.public_ip
        p_ipv4_name = ctk.CTkLabel(frame_public, text="Your Public IPv4", anchor="w")
        p_ipv4_name.grid(column=0, row=1, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        p_ipv4_name.configure(font=self.poppins_200)

        p_ipv4_value = ctk.CTkLabel(frame_public, text="112.119.24.31", anchor="w")
        p_ipv4_value.grid(column=1, row=1, sticky="nesw", padx=(0, 10), pady=(0, 5))
        p_ipv4_value.configure(font=self.poppins_300)

        p_ipv4_name.bind("<Enter>", lambda event: hover.display(tooltips["pub_ipv4"]))
        p_ipv4_name.bind("<Leave>", lambda event: hover.display(""))

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
        label_geoip = ctk.CTkLabel(frame_geoip, text="IP Geolocation", anchor="w")
        label_geoip.configure(font=self.poppins_400, text_color=TEXT_CLR_700)
        label_geoip.grid(columnspan=2, rowspan=1, sticky="nesw", padx=(LP), pady=(10))

        # Continent & Continent Code
        # continent = self.geolocation_data.continent
        continent = "Asia"
        # continent_code = self.geolocation_data.continent_code
        continent_code = "AS"
        continent_name = ctk.CTkLabel(frame_geoip, text="Continent", anchor="w")
        continent_name.grid(column=0, row=2, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        continent_name.configure(font=self.poppins_200)

        continent_value = ctk.CTkLabel(
            frame_geoip, text=f"{continent} ({continent_code})", anchor="w"
        )

        continent_value.grid(column=1, row=2, sticky="nesw", padx=(0, 10), pady=(0, 5))
        continent_value.configure(font=self.poppins_300)

        # country = self.geolocation_data.country
        country = "Sri Lanka"
        # country_code = self.geolocation_data.country_code
        country_code = "LK"
        country_name = ctk.CTkLabel(frame_geoip, text="Country", anchor="w")
        country_name.grid(column=0, row=3, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        country_name.configure(font=self.poppins_200)

        country_value = ctk.CTkLabel(
            frame_geoip, text=f"{country} ({country_code})", anchor="w"
        )
        country_value.grid(column=1, row=3, sticky="nesw", padx=(0, 10), pady=(0, 5))
        country_value.configure(font=self.poppins_300)

        # region = self.geolocation_data.region_name
        region = "Western Province"
        region_name = ctk.CTkLabel(frame_geoip, text="Region", anchor="w")
        region_name.grid(column=0, row=4, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        region_name.configure(font=self.poppins_200)

        region_value = ctk.CTkLabel(frame_geoip, text=region, anchor="w")
        region_value.grid(column=1, row=4, sticky="nesw", padx=(0, 10), pady=(0, 5))
        region_value.configure(font=self.poppins_300)

        # city = self.geolocation_data.city
        city = "Battaramulla South"
        city_name = ctk.CTkLabel(frame_geoip, text="City", anchor="w")
        city_name.grid(column=0, row=5, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        city_name.configure(font=self.poppins_200)

        city_value = ctk.CTkLabel(frame_geoip, text=city, anchor="w")
        city_value.grid(column=1, row=5, sticky="nesw", padx=(0, 10), pady=(0, 5))
        city_value.configure(font=self.poppins_300)

        # district = self.geolocation_data.district
        district = "-"
        district_name = ctk.CTkLabel(frame_geoip, text="District", anchor="w")
        district_name.grid(column=0, row=6, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        district_name.configure(font=self.poppins_200)

        district_value = ctk.CTkLabel(frame_geoip, text=district, anchor="w")
        district_value.grid(column=1, row=6, sticky="nesw", padx=(0, 10), pady=(0, 5))
        district_value.configure(font=self.poppins_300)

        # zipcode = self.geolocation_data.zipcode
        zipcode = "10120"
        zip_name = ctk.CTkLabel(frame_geoip, text="Zip", anchor="w")
        zip_name.grid(column=0, row=7, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        zip_name.configure(font=self.poppins_200)

        zip_value = ctk.CTkLabel(frame_geoip, text=zipcode, anchor="w")
        zip_value.grid(column=1, row=7, sticky="nesw", padx=(0, 10), pady=(0, 5))
        zip_value.configure(font=self.poppins_300)

        # lat = self.geolocation_data.lat
        lat = "80.6554"
        lat_name = ctk.CTkLabel(frame_geoip, text="Latitude", anchor="w")
        lat_name.grid(column=0, row=8, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        lat_name.configure(font=self.poppins_200)

        lat_value = ctk.CTkLabel(frame_geoip, text=lat, anchor="w")
        lat_value.grid(column=1, row=8, sticky="nesw", padx=(0, 10), pady=(0, 5))
        lat_value.configure(font=self.poppins_300)

        # lon = self.geolocation_data.lon
        lon = "6.98"
        lon_name = ctk.CTkLabel(frame_geoip, text="Longitude", anchor="w")
        lon_name.grid(column=0, row=9, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        lon_name.configure(font=self.poppins_200)

        lon_value = ctk.CTkLabel(frame_geoip, text=lon, anchor="w")
        lon_value.grid(column=1, row=9, sticky="nesw", padx=(0, 10), pady=(0, 5))
        lon_value.configure(font=self.poppins_300)

        # timezone = self.geolocation_data.timezone
        timezone = "Asia/AS"
        timezone_name = ctk.CTkLabel(frame_geoip, text="Timezone", anchor="w")
        timezone_name.grid(column=0, row=10, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        timezone_name.configure(font=self.poppins_200)

        timezone_value = ctk.CTkLabel(frame_geoip, text=timezone, anchor="w")
        timezone_value.grid(column=1, row=10, sticky="nesw", padx=(0, 10), pady=(0, 5))
        timezone_value.configure(font=self.poppins_300)

        # currency = self.geolocation_data.currency
        currency = "LK"
        currency_name = ctk.CTkLabel(frame_geoip, text="Currency", anchor="w")
        currency_name.grid(column=0, row=11, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        currency_name.configure(font=self.poppins_200)

        currency_value = ctk.CTkLabel(frame_geoip, text=currency, anchor="w")
        currency_value.grid(column=1, row=11, sticky="nesw", padx=(0, 10), pady=(0, 5))
        currency_value.configure(font=self.poppins_300)

        # isp = self.geolocation_data.isp
        isp = "SLT - Sri Lanka Telecom"
        isp_name = ctk.CTkLabel(frame_geoip, text="ISP", anchor="w")
        isp_name.grid(column=2, row=2, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        isp_name.configure(font=self.poppins_200)

        isp_value = ctk.CTkLabel(frame_geoip, text=isp, anchor="w")
        isp_value.grid(column=3, row=2, sticky="nesw", padx=(0, 10), pady=(0, 5))
        isp_value.configure(font=self.poppins_300)

        isp_name.bind("<Enter>", lambda event: hover.display(tooltips["isp"]))
        isp_name.bind("<Leave>", lambda event: hover.display(""))

        # org = self.geolocation_data.org
        org = "-"
        org_name = ctk.CTkLabel(frame_geoip, text="Organization", anchor="w")
        org_name.grid(column=2, row=3, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        org_name.configure(font=self.poppins_200)

        org_value = ctk.CTkLabel(frame_geoip, text=org, anchor="w")
        org_value.grid(column=3, row=3, sticky="nesw", padx=(0, 10), pady=(0, 5))
        org_value.configure(font=self.poppins_300)

        # asn = self.geolocation_data.asn
        asn = "SLT123"
        asn_name = ctk.CTkLabel(frame_geoip, text="ASN", anchor="w")
        asn_name.grid(column=2, row=4, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        asn_name.configure(font=self.poppins_200)

        asn_value = ctk.CTkLabel(frame_geoip, text=asn, anchor="w")
        asn_value.grid(column=3, row=4, sticky="nesw", padx=(0, 10), pady=(0, 5))
        asn_value.configure(font=self.poppins_300)

        asn_name.bind("<Enter>", lambda event: hover.display(tooltips["asn"]))
        asn_name.bind("<Leave>", lambda event: hover.display(""))

        # asname = self.geolocation_data.as_name
        asname = "SLT"
        asname_name = ctk.CTkLabel(frame_geoip, text="AS Name", anchor="w")
        asname_name.grid(column=2, row=5, sticky="nesw", padx=(LP, 0), pady=(0, 5))
        asname_name.configure(font=self.poppins_200)

        asname_value = ctk.CTkLabel(frame_geoip, text=asname, anchor="w")
        asname_value.grid(column=3, row=5, sticky="nesw", padx=(0, 10), pady=(0, 5))
        asname_value.configure(font=self.poppins_300)

        asname_name.bind("<Enter>", lambda event: hover.display(tooltips["as_name"]))
        asname_name.bind("<Leave>", lambda event: hover.display(""))
