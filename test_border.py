import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("High Level Tool")
window.geometry("1000x600")


class MainFrame(ttk.Frame):
    def __init__(self, parent, border_color):
        super().__init__(parent)
        style = ttk.Style()
        style.configure(
            "Custom.TFrame", borderwidth=200, relief="sunken", foreground="red"
        )
        self.configure(style="Custom.TFrame")
        self.place(relx=0, rely=0, relheight=1, relwidth=1)


MainFrame(window, "blue")

window.mainloop()
