import customtkinter as ctk


SIDEBAR_WIDTH = 0.15
CURRENT_FRAME_HEIGHT = 0.95


class CurrentFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(corner_radius=0, fg_color="#242424")
        self.place(
            relx=SIDEBAR_WIDTH,
            rely=0,
            relwidth=(1 - SIDEBAR_WIDTH),
            relheight=CURRENT_FRAME_HEIGHT,
        )
