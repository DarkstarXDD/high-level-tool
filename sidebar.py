import customtkinter as ctk


SIDEBAR_WIDTH = 0.15


class Sidebar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(corner_radius=0)
        self.place(relx=0, rely=0, relwidth=SIDEBAR_WIDTH, relheight=1)
