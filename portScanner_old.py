import tkinter as tk
from tkinter import ttk


BG_CLR = "#232425"
TEXT_CLR_100 = "#FFFFFF"
TEXT_CLR_200 = "#DEE2E6"
LABEL_FF = "Poppins"
LABEL_FS = 10
ENTRY_BG_CLR = "#313335"


class PortScanner(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.configure(style="portscannerframe.TFrame")

        self.columnconfigure(0, weight=1, uniform="a")
        self.rowconfigure(0, weight=2, uniform="a")
        self.rowconfigure(1, weight=3, uniform="a")
        self.rowconfigure(2, weight=1, uniform="a")

        # --------------- Style Classes ---------------
        style = ttk.Style()
        style.configure(
            "portscannerframe.TFrame",
            background=BG_CLR,
        )
        style.configure(
            "subframe.TFrame",
            background=BG_CLR,
            borderwidth=1,
            relief="solid",
        )
        style.configure(
            "label.TLabel",
            background=BG_CLR,
            foreground=TEXT_CLR_200,
        )

        # --------------- Create 3 Sections ---------------
        frame_top = ttk.Frame(self)
        frame_top.configure(style="subframe.TFrame")
        frame_top.grid(row=0, column=0, sticky="nesw", padx=5, pady=5)

        frame_middle = ttk.Frame(self)
        frame_middle.configure(style="subframe.TFrame")
        frame_middle.grid(row=1, column=0, sticky="nesw", padx=5, pady=5)

        frame_bottom = ttk.Frame(self)
        frame_bottom.configure(style="subframe.TFrame")
        frame_bottom.grid(row=2, column=0, sticky="nesw", padx=5, pady=5)

        # --------------- Create Labels, Inputs & BUTTONS ---------------
        frame_top.columnconfigure(0, weight=1, uniform="a")
        frame_top.columnconfigure(1, weight=2, uniform="a")
        frame_top.rowconfigure((0, 1, 2), weight=1)

        # Labels
        self.label_target = ttk.Label(frame_top, text="Target IP", style="label.TLabel")
        self.label_start = ttk.Label(frame_top, text="Start Port", style="label.TLabel")
        self.label_end = ttk.Label(frame_top, text="End Port", style="label.TLabel")

        self.label_target.grid(row=0, column=0, sticky="nesw", padx=5, pady=5)
        self.label_start.grid(row=1, column=0, sticky="nesw", padx=5, pady=5)
        self.label_end.grid(row=2, column=0, sticky="nesw", padx=5, pady=5)

        # Inputs
        self.input_target = tk.Entry(
            frame_top, background=ENTRY_BG_CLR, foreground=TEXT_CLR_100
        )
        self.input_start = tk.Entry(
            frame_top, background=ENTRY_BG_CLR, foreground=TEXT_CLR_100
        )
        self.input_end = tk.Entry(
            frame_top, background=ENTRY_BG_CLR, foreground=TEXT_CLR_100
        )

        self.input_target.grid(row=0, column=1, sticky="nesw", padx=5, pady=5)
        self.input_start.grid(row=1, column=1, sticky="nesw", padx=5, pady=5)
        self.input_end.grid(row=2, column=1, sticky="nesw", padx=5, pady=5)
