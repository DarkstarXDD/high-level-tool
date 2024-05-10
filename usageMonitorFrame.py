import time
import threading

import psutil

import customtkinter as ctk


class UsageMonitor:
    def __init__(self, update_callback=None):
        self.total = 0
        self.total_upload = 0
        self.total_download = 0
        self.loop_running = False
        self.update_callback = update_callback

    def start_monitoring(self):
        self.loop_running = True

        # 'psutil.net_io_counters()' returns values since last system restart.
        last_counters = psutil.net_io_counters()

        while self.loop_running:
            new_counters = psutil.net_io_counters()

            new_received = new_counters.bytes_recv - last_counters.bytes_recv
            new_sent = new_counters.bytes_sent - last_counters.bytes_sent
            new_total = new_received + new_sent

            # Bytes --> KB --> MB
            new_received_in_mb = new_received / 1024 / 1024
            new_sent_in_mb = new_sent / 1024 / 1024
            new_total_in_mb = new_total / 1024 / 1024

            self.total += new_total_in_mb
            self.total_download += new_received_in_mb
            self.total_upload += new_sent_in_mb

            if self.update_callback:
                self.update_callback(
                    {
                        "total": self.total,
                        "total_upload": self.total_upload,
                        "total_download": self.total_download,
                    }
                )

            last_counters = new_counters
            time.sleep(1)

    def stop_monitoring(self):
        self.loop_running = False


class UsageMonitorFrame(ctk.CTkFrame):
    def __init__(self, parent, hover, tooltips):
        super().__init__(parent)

        self.usage_monitor = UsageMonitor(update_callback=self.update_labels)

        # Bind the destroy event of the window to a function
        self.bind("<Destroy>", self.on_window_close)

        # ------------------------------------------------------------------------
        # -------------------------------- GUI -----------------------------------
        # ------------------------------------------------------------------------
        self.poppins_300 = ctk.CTkFont(family="Poppins Medium", size=14)
        self.poppins_200 = ctk.CTkFont(family="Poppins", size=14)
        self.poppins_400 = ctk.CTkFont(family="Poppins SemiBold", size=18)
        self.cascadia_200 = ctk.CTkFont(family="Cascadia Mono", size=14)

        self.configure(corner_radius=0, fg_color="#242424")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.columnconfigure(0, weight=1, uniform="a")
        self.rowconfigure(0, weight=2, uniform="a")
        self.rowconfigure(1, weight=3, uniform="a")
        self.rowconfigure(2, weight=4, uniform="a")

        # ------------------------ 3 Frames for the Sections -----------------------
        self.frame_top = ctk.CTkFrame(self)
        self.frame_top.grid(row=0, sticky="nesw", padx=10, pady=(10, 5))

        self.frame_top.columnconfigure(0, weight=1, uniform="a")
        self.frame_top.columnconfigure(1, weight=1, uniform="a")
        self.frame_top.rowconfigure(0, weight=1, uniform="a")

        self.frame_middle = ctk.CTkFrame(self)
        self.frame_middle.grid(row=1, sticky="nesw", padx=10, pady=5)

        self.frame_middle.columnconfigure(0, weight=1, uniform="a")
        self.frame_middle.columnconfigure(1, weight=1, uniform="a")
        self.frame_middle.rowconfigure(0, weight=1, uniform="a")
        self.frame_middle.rowconfigure(1, weight=1, uniform="a")

        self.frame_bottom = ctk.CTkFrame(self)
        self.frame_bottom.grid(row=2, sticky="nesw", padx=10, pady=(5, 10))
        self.frame_bottom.configure(fg_color="#242424")

        # ---------------------- Buttons ------------------------
        self.button_start = ctk.CTkButton(self.frame_top)
        self.button_start.configure(
            text="Start",
            font=self.poppins_400,
            fg_color="#314724",
            hover_color="#26361B",
            command=self.handle_start_click,
        )
        self.button_start.grid(row=0, column=0, sticky="nesw", padx=(80, 40), pady=20)

        self.button_stop = ctk.CTkButton(self.frame_top)
        self.button_stop.configure(
            text="Stop",
            font=self.poppins_400,
            fg_color="#70292A",
            hover_color="#592122",
            state="disabled",
            command=self.handle_stop_click,
        )
        self.button_stop.grid(row=0, column=1, sticky="nesw", padx=(40, 80), pady=20)

        # ----------------------- Labels --------------------------
        self.lbl_total = self.create_label("Total")
        self.lbl_total.grid(row=0, column=0, sticky="nesw", padx=80, pady=5)
        self.lbl_total.bind(
            "<Enter>", lambda event: hover.display(tooltips["usage_total"])
        )
        self.lbl_total.bind("<Leave>", lambda event: hover.display(""))

        self.lbl_upload = self.create_label("Total Upload")
        self.lbl_upload.grid(row=0, column=1, sticky="nesw", padx=40, pady=5)
        self.lbl_upload.bind(
            "<Enter>", lambda event: hover.display(tooltips["usage_upload"])
        )
        self.lbl_upload.bind("<Leave>", lambda event: hover.display(""))

        self.lbl_download = self.create_label("Total Download")
        self.lbl_download.grid(row=1, column=1, sticky="nesw", padx=40, pady=5)
        self.lbl_download.bind(
            "<Enter>", lambda event: hover.display(tooltips["usage_download"])
        )
        self.lbl_download.bind("<Leave>", lambda event: hover.display(""))

    def create_label(self, label_text):
        label = ctk.CTkLabel(
            self.frame_middle,
            text=f"{label_text}: 0.00 MB",
            anchor="w",
        )
        label.configure(font=self.poppins_400)
        return label

    def update_labels(self, data):
        self.lbl_total.configure(text=f"Total: {data['total']:.2f} MB")
        self.lbl_upload.configure(text=f"Total Upload: {data['total_upload']:.2f} MB")
        self.lbl_download.configure(
            text=f"Total Download: {data['total_download']:.2f} MB"
        )

    def handle_start_click(self):
        self.button_start.configure(state="disabled")
        self.button_stop.configure(state="normal")
        threading.Thread(target=self.usage_monitor.start_monitoring).start()

    def handle_stop_click(self):
        self.button_start.configure(state="normal")
        self.button_stop.configure(state="disabled")
        self.usage_monitor.stop_monitoring()

    def on_window_close(self, event):
        self.usage_monitor.stop_monitoring()
        print("Window closed successfuly")
