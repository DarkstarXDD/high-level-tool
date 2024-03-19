import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, sidebar_width):
        super().__init__(parent)

        self.configure(corner_radius=0)
        self.place(relx=0, rely=0, relwidth=sidebar_width, relheight=1)
