# pylint: disable=no-member

import re
import threading
import scapy.all as scapy
from tabulate import tabulate

import customtkinter as ctk


class PingSweepFrame(ctk.CTkFrame):
    def __init__(self, parent, hover, tooltips, descriptions):
        super().__init__(parent)

        self.poppins_300 = ctk.CTkFont(family="Poppins Medium", size=14)
        self.poppins_200 = ctk.CTkFont(family="Poppins", size=14)
        self.poppins_400 = ctk.CTkFont(family="Poppins SemiBold", size=18)
        self.cascadia_200 = ctk.CTkFont(family="Cascadia Mono", size=14)

        self.configure(corner_radius=0, fg_color="#242424")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.columnconfigure(0, weight=1, uniform="a")
        self.rowconfigure(0, weight=4, uniform="a")
        self.rowconfigure(1, weight=6, uniform="a")
        self.rowconfigure(2, weight=3, uniform="a")

        # ------------------------ 3 Frames for the Sections -----------------------
        frame_top = ctk.CTkFrame(self)
        frame_top.grid(row=0, sticky="nesw", padx=10, pady=(10, 5))

        frame_top.columnconfigure(0, weight=1, uniform="a")
        frame_top.columnconfigure(1, weight=2, uniform="a")
        frame_top.columnconfigure(2, weight=2, uniform="a")
        frame_top.rowconfigure((0, 1, 2), weight=1, uniform="a")

        frame_middle = ctk.CTkFrame(self)
        frame_middle.grid(row=1, sticky="nesw", padx=10, pady=5)
        frame_middle.configure(fg_color="#242424")

        frame_bottom = ctk.CTkFrame(self)
        frame_bottom.grid(row=2, sticky="nesw", padx=10, pady=(5, 10))
        frame_bottom.configure(fg_color="#242424")

        # -------------------------------- Labels --------------------------------
        lbl_range = ctk.CTkLabel(frame_top, text="IP Address Range", anchor="w")
        lbl_range.configure(font=self.poppins_200)
        lbl_range.grid(row=0, column=0, sticky="nesw", padx=15, pady=5)

        lbl_range.bind("<Enter>", lambda event: hover.display(tooltips["pingsweep"]))
        lbl_range.bind("<Leave>", lambda event: hover.display(""))

        # -------------------------------- Inputs --------------------------------
        self.input_target = ctk.CTkEntry(frame_top)
        self.input_target.insert(0, "192.168.1.0/24")
        self.input_target.grid(row=0, column=1, sticky="nesw", padx=5, pady=5)

        # -------------------------------- Buttons --------------------------------
        self.button_reset = ctk.CTkButton(frame_top)
        self.button_reset.configure(
            text="Reset",
            font=self.poppins_400,
            command=self.handle_reset_click,
        )
        self.button_reset.grid(row=0, column=2, sticky="nesw", padx=(100, 10), pady=5)

        self.button_start = ctk.CTkButton(frame_top)
        self.button_start.configure(
            text="Run Ping Sweep",
            font=self.poppins_400,
            fg_color="#314724",
            hover_color="#26361B",
            command=self.handle_start_click,
        )
        self.button_start.grid(row=1, column=2, sticky="nesw", padx=(100, 10), pady=5)

        self.button_cancel = ctk.CTkButton(frame_top)
        self.button_cancel.configure(
            text="Cancel",
            font=self.poppins_400,
            fg_color="#70292A",
            hover_color="#592122",
            state="disabled",
        )
        self.button_cancel.grid(row=2, column=2, sticky="nesw", padx=(100, 10), pady=5)

        # ------------------------------ Main Output ------------------------------
        self.main_output = ctk.CTkTextbox(frame_middle, font=self.cascadia_200)
        self.main_output.pack(expand=True, fill="both")

        # ------------------------------ Description ------------------------------
        txtbox_description = ctk.CTkTextbox(frame_bottom, font=self.poppins_200)
        txtbox_description.insert("end", descriptions["ping_sweep"])
        txtbox_description.configure(fg_color="#2b2b2b", state="disabled")
        txtbox_description.pack(expand=True, fill="both")

    def run_pingsweep(self):
        target_range = self.input_target.get()
        self.main_output.delete("1.0", "end")

        try:
            # Regular Expression Pattern to recognize IPv4 addresses.
            ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}/[0-9]*$")

            # Check whether target is valid
            if ip_add_range_pattern.search(target_range):
                arp_result = scapy.arping(target_range, verbose=False)

                # Process the ARP result to extract MAC addresses and IP addresses
                arp_table = []
                for _, received in arp_result[0]:
                    arp_table.append([received.psrc, received.hwsrc])

                arp_table_sorted = sorted(arp_table, key=lambda x: x[0])

                # Display the ARP result in a table format
                result = tabulate(
                    arp_table_sorted,
                    headers=["IP Address", "MAC Address"],
                    tablefmt="grid",
                )
                self.main_output.insert("end", result)

            else:
                self.main_output.insert("end", "IP Address range invalid!")

        except Exception as error:
            print("An error occurred:", error)
            self.main_output.insert("end", error)

        self.button_start.configure(state="normal")
        self.button_reset.configure(state="normal")

    def handle_reset_click(self):
        self.main_output.delete("1.0", "end")
        self.input_target.delete(0, "end")
        self.input_target.insert(0, "192.168.1.0/24")

    def handle_start_click(self):
        self.button_start.configure(state="disabled")
        self.button_reset.configure(state="disabled")
        threading.Thread(target=self.run_pingsweep).start()
