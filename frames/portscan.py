import socket
import threading
import queue

import customtkinter as ctk

PORTSCAN_THREAD_COUNT = 100


class PortScannerFrame(ctk.CTkFrame):
    def __init__(self, parent, hover, tooltips, descriptions):
        super().__init__(parent)

        self.running = False  # Flag for stopping scan mid execution

        self.poppins_200 = ctk.CTkFont(family="Poppins", size=14)
        self.poppins_300 = ctk.CTkFont(family="Poppins Medium", size=14)
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
        label_target = ctk.CTkLabel(frame_top, text="Target IP", anchor="w")
        label_target.configure(font=self.poppins_200)
        label_target.bind(
            "<Enter>", lambda event: hover.display(tooltips["port_target"])
        )
        label_target.bind("<Leave>", lambda event: hover.display(""))
        label_target.grid(row=0, column=0, sticky="nesw", padx=15, pady=5)

        label_start = ctk.CTkLabel(frame_top, text="Start Port", anchor="w")
        label_start.configure(font=self.poppins_200)
        label_start.bind("<Enter>", lambda event: hover.display(tooltips["port_start"]))
        label_start.bind("<Leave>", lambda event: hover.display(""))
        label_start.grid(row=1, column=0, sticky="nesw", padx=15, pady=5)

        label_end = ctk.CTkLabel(frame_top, text="End Port", anchor="w")
        label_end.configure(font=self.poppins_200)
        label_end.bind("<Enter>", lambda event: hover.display(tooltips["port_end"]))
        label_end.bind("<Leave>", lambda event: hover.display(""))
        label_end.grid(row=2, column=0, sticky="nesw", padx=15, pady=5)

        # -------------------------------- Inputs --------------------------------
        self.input_target = ctk.CTkEntry(frame_top)
        self.input_target.insert(0, "192.168.1.1")
        self.input_target.grid(row=0, column=1, sticky="nesw", padx=5, pady=5)

        self.input_start = ctk.CTkEntry(frame_top)
        self.input_start.insert(0, "1")
        self.input_start.grid(row=1, column=1, sticky="nesw", padx=5, pady=5)

        self.input_end = ctk.CTkEntry(frame_top)
        self.input_end.insert(0, "1024")
        self.input_end.grid(row=2, column=1, sticky="nesw", padx=5, pady=5)

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
            text="Start",
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
            command=self.stop_scan,
        )
        self.button_cancel.grid(row=2, column=2, sticky="nesw", padx=(100, 10), pady=5)

        # ----------------------------- Main Output -----------------------------
        self.main_output = ctk.CTkTextbox(frame_middle, font=self.cascadia_200)
        self.main_output.pack(expand=True, fill="both")

        # ------------------------------ Description -----------------------------
        txtbox_description = ctk.CTkTextbox(frame_bottom, font=self.poppins_200)
        txtbox_description.insert("end", descriptions["port_scan"])
        txtbox_description.configure(fg_color="#2b2b2b", state="disabled")
        txtbox_description.pack(expand=True, fill="both")

    def run_port_scan(self):
        self.running = True
        self.button_start.configure(state="disabled")
        self.button_reset.configure(state="disabled")
        self.button_cancel.configure(state="normal")
        target_ip = self.input_target.get()
        starting_port = self.input_start.get()
        ending_port = self.input_end.get()

        self.main_output.delete("1.0", "end")

        PortScan(
            target_ip, starting_port, ending_port, self.main_output, self.stop_flag
        )
        print("Port Scan is done!")

        if self.running:
            self.main_output.insert("end", "\nPort Scan is done!")
            print("Port Scan is done!")
        else:
            self.main_output.insert("end", "\nPort Scan was Interrupted!")
            print("Port Scan was interrupted!")

        self.button_start.configure(state="normal")
        self.button_cancel.configure(state="disabled")
        self.button_reset.configure(state="normal")

    # --------- Run the port scan in a new thread. So the GUI won't freeze ---------
    def handle_start_click(self):
        threading.Thread(target=self.run_port_scan).start()

    def stop_scan(self):
        self.running = False

    def stop_flag(self):
        return not self.running

    def handle_reset_click(self):
        self.main_output.delete("1.0", "end")

        self.input_target.delete(0, "end")
        self.input_target.insert(0, "192.168.1.1")

        self.input_start.delete(0, "end")
        self.input_start.insert(0, "1")

        self.input_end.delete(0, "end")
        self.input_end.insert(0, "1024")


class PortScan:
    def __init__(self, ip, start, end, main_output, stop_flag):

        self.main_output = main_output

        self.stop_flag = stop_flag

        self.target_ip = str(ip)
        self.port_start = int(start)
        self.port_end = int(end)

        self.open_ports = []
        self.new_queue = queue.Queue()
        self.thread_list = []

        # Create the port list & add the ports to the queue
        port_list = range(self.port_start, self.port_end)
        self.fill_queue(port_list)

        for _ in range(PORTSCAN_THREAD_COUNT):
            thread = threading.Thread(target=self.worker)
            self.thread_list.append(thread)

        for thread in self.thread_list:
            thread.start()

        for thread in self.thread_list:
            thread.join()

    def scan_port(self, port):
        try:
            new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            new_socket.settimeout(1)
            new_socket.connect((self.target_ip, port))
            new_socket.close()
            return True

        except:
            return False

    def fill_queue(self, port_list):
        for port in port_list:
            self.new_queue.put(port)

    def worker(self):
        while not self.new_queue.empty() and not self.stop_flag():
            port = self.new_queue.get()

            if self.scan_port(port):
                print(f"Port {port} is open!")
                self.main_output.insert(
                    "end", f" \nPort {port} on {self.target_ip} is open!"
                )
                self.open_ports.append(port)
