import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Entry Widget Test")
window.geometry("400x500")


input_1 = tk.Entry(window)
input_1.pack(expand=True, fill="x", padx=10)
input_1.configure(background="red", foreground="green")

window.mainloop()
