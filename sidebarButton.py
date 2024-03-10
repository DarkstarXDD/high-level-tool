import customtkinter as ctk


class SidebarButton(ctk.CTkButton):

    active_button = None

    def __init__(self, parent, button_text, frame_to_raise):
        super().__init__(parent)

        self.configure(
            parent,
            text=button_text,
            fg_color="transparent",
            command=lambda: self.handle_click(frame_to_raise),
            anchor="w",
        )
        self.pack(expand=True, fill="both")

    def handle_click(self, frame_to_raise):
        frame_to_raise.lift()

        if SidebarButton.active_button is not None:
            SidebarButton.active_button.configure(fg_color="transparent")

        self.configure(fg_color="#144870")
        SidebarButton.active_button = self
