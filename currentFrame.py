import customtkinter as ctk


class CurrentFrame(ctk.CTkFrame):
    def __init__(self, parent, sidebar_width, current_frame_height):
        super().__init__(parent)

        self.configure(corner_radius=0, fg_color="#242424")
        self.place(
            relx=sidebar_width,
            rely=0,
            relwidth=(1 - sidebar_width),
            relheight=current_frame_height,
        )
