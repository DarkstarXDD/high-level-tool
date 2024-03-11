import customtkinter as ctk
import socket
import threading
import queue


class PortScannerFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(corner_radius=0, fg_color="#242424")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.columnconfigure(0, weight=1, uniform="a")
        self.rowconfigure(0, weight=2, uniform="a")
        self.rowconfigure(1, weight=4, uniform="a")
        self.rowconfigure(2, weight=1, uniform="a")

        # Create 3 Frames for the Sections
        frame_top = ctk.CTkFrame(self)
        frame_middle = ctk.CTkFrame(self)
        frame_bottom = ctk.CTkFrame(self)

        # Place the 3 Frames (Sections)
        frame_top.grid(row=0, sticky="nesw", padx=10, pady=(10, 5))
        frame_middle.grid(row=1, sticky="nesw", padx=10, pady=5)
        frame_bottom.grid(row=2, sticky="nesw", padx=10, pady=(5, 10))

        # --------------- Create & Place Labels ---------------
        frame_top.columnconfigure(0, weight=1, uniform="a")
        frame_top.columnconfigure(1, weight=2, uniform="a")
        frame_top.columnconfigure(2, weight=2, uniform="a")
        frame_top.rowconfigure((0, 1, 2), weight=1, uniform="a")

        label_target = ctk.CTkLabel(frame_top, text="Target IP")
        label_start = ctk.CTkLabel(frame_top, text="Start Port")
        label_end = ctk.CTkLabel(frame_top, text="End Port")

        label_target.grid(row=0, column=0, sticky="nesw", padx=5, pady=5)
        label_start.grid(row=1, column=0, sticky="nesw", padx=5, pady=5)
        label_end.grid(row=2, column=0, sticky="nesw", padx=5, pady=5)

        # --------------- Create & Place Inputs ---------------
        self.input_target = ctk.CTkEntry(frame_top)
        self.input_start = ctk.CTkEntry(frame_top)
        self.input_end = ctk.CTkEntry(frame_top)

        self.input_target.grid(row=0, column=1, sticky="nesw", padx=5, pady=5)
        self.input_start.grid(row=1, column=1, sticky="nesw", padx=5, pady=5)
        self.input_end.grid(row=2, column=1, sticky="nesw", padx=5, pady=5)

        # --------------- Create & Place Buttons ---------------
        self.button_reset = ctk.CTkButton(frame_top)
        self.button_reset.configure(text="Reset")

        self.button_start = ctk.CTkButton(frame_top)
        self.button_start.configure(
            text="Start",
            fg_color="#314724",
            hover_color="#26361B",
            command=self.handle_start_click,
        )

        self.button_cancel = ctk.CTkButton(frame_top)
        self.button_cancel.configure(
            text="Cancel", fg_color="#70292A", hover_color="#592122"
        )

        self.button_reset.grid(row=0, column=2, sticky="nesw", padx=(100, 10), pady=5)
        self.button_start.grid(row=1, column=2, sticky="nesw", padx=(100, 10), pady=5)
        self.button_cancel.grid(row=2, column=2, sticky="nesw", padx=(100, 10), pady=5)

        # PortScan()

    def handle_start_click(self):
        target_ip = self.input_target.get()
        starting_port = self.input_start.get()
        ending_port = self.input_end.get()

        PortScan(target_ip, starting_port, ending_port)
        print("Port Scan is done!")


class PortScan:
    def __init__(self, ip, start, end):

        self.target_ip = str(ip)
        self.port_start = int(start)
        self.port_end = int(end)

        self.open_ports = []
        self.new_queue = queue.Queue()
        self.thread_list = []

        # Create the port list & add the ports to the queue
        port_list = range(self.port_start, self.port_end)
        self.fill_queue(port_list)

        for t in range(100):
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
        while not self.new_queue.empty():
            port = self.new_queue.get()

            if self.scan_port(port):
                print(f"Port {port} is open!")
                self.open_ports.append(port)
