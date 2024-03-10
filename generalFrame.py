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
