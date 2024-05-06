import customtkinter as ctk


class HoverArea(ctk.CTkFrame):
    def __init__(self, parent, sidebar_width, current_frame_height):
        super().__init__(parent)

        self.configure(corner_radius=0, fg_color="#242424")
        self.place(
            relx=sidebar_width,
            rely=current_frame_height,
            relwidth=(1 - sidebar_width),
            relheight=(1 - current_frame_height),
        )

        self.columnconfigure(0, weight=1, uniform="a")
        self.rowconfigure(0, weight=1, uniform="a")

        frame = ctk.CTkFrame(self)
        frame.grid(sticky="nesw", column=0, row=0, padx=10, pady=(0, 10))
        frame.configure(fg_color="#242424")

        self.display_txt = ctk.CTkLabel(frame, text="", anchor="w")
        self.display_txt.configure(padx=15)
        self.display_txt.pack(expand=True, fill="both")

    # Call this method inside any frame, to update the hover text
    # make sure to pass the hoverArea as a argument for all the frames inside the start.py
    def display(self, text):
        self.display_txt.configure(text=text)
