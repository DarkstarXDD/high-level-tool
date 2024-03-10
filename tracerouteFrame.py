import customtkinter as ctk


class TracerouteFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(corner_radius=0, fg_color="#242424")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        label = ctk.CTkLabel(self, text="Traceroute")
        label.pack()
