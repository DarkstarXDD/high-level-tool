import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("High Level Tool")
window.geometry("1000x600")
# window.resizable(False, False)

BG_COLOR = "#232425"
TEXT_COLOR_100 = "#FFFFFF"
TEXT_CLR_SIDEBAR = "#C9D1D9"
TEXT_CLR_SIDEBAR_HOVER = "#F3F5F6"
FONT_SIZE_SIDEBAR = 12
SIDEBAR_BUTTON_ACTIVE_CLR = "#313335"
PRIMARY_BLUE = "#4E8FE4"


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

        self.place(relx=0, rely=0, relwidth=0.2, relheight=1)


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
                font=("Poppins SemiBold", FONT_SIZE_SIDEBAR),
            )

    def handle_leave(self, event):
        if SidebarButton.active_button != self:
            self.style.configure(
                self.instance_style_name,
                background=BG_COLOR,
                foreground=TEXT_CLR_SIDEBAR,
                font=("Poppins", FONT_SIZE_SIDEBAR),
            )

    def handle_click(self, event):
        if SidebarButton.active_button is not None:
            SidebarButton.active_button.style.configure(
                SidebarButton.active_button.instance_style_name,
                background=BG_COLOR,
                foreground=TEXT_CLR_SIDEBAR,
                font=("Poppins", FONT_SIZE_SIDEBAR),
            )

        self.style.configure(
            self.instance_style_name,
            background=SIDEBAR_BUTTON_ACTIVE_CLR,
            foreground=PRIMARY_BLUE,
            font=("Poppins SemiBold", FONT_SIZE_SIDEBAR),
        )

        SidebarButton.active_button = self


mainframe = MainFrame(window)
sidebar = Sidebar(mainframe)

# Sidebar Buttons
btn_general = SidebarButton(sidebar, "General")
btn_network_interface = SidebarButton(sidebar, "Network Interfaces")
btn_wifi = SidebarButton(sidebar, "Wifi")
btn_ip_scanner = SidebarButton(sidebar, "IP Scanner")
btn_port_scanner = SidebarButton(sidebar, "Port Scanner")
btn_ping = SidebarButton(sidebar, "Ping")
btn_traceroute = SidebarButton(sidebar, "Traceroute")
btn_mac_lookup = SidebarButton(sidebar, "MAC Address Lookup")

window.mainloop()
