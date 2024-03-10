import customtkinter as ctk


class SidebarButton(ctk.CTkButton):
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

        # Bind left mouse button click event to this instance
        self.bind("<Button-1>", lambda event: self.handle_click(frame_to_raise))

    def handle_click(self, frame_to_raise):
        frame_to_raise.lift()
        self.configure(fg_color="green")


# Example usage
# Assuming root is your Tkinter root window
root = ctk.CTk()

frame1 = ctk.CTkFrame(root, bg="red", width=200, height=200)
frame2 = ctk.CTkFrame(root, bg="blue", width=200, height=200)
frame1.place(x=0, y=0)
frame2.place(x=200, y=0)

button1 = SidebarButton(frame1, "Button 1", frame1)
button2 = SidebarButton(frame2, "Button 2", frame2)

root.mainloop()
