import tkinter as tk


def show_text(event):
    status_label.config(text="This is the IP Address the internet will see.")


def hide_text(event):
    status_label.config(text="")


root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="Public IP Address", font=("Arial", 12))
label.pack(pady=20)

status_label = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X)

label.bind("<Enter>", show_text)
label.bind("<Leave>", hide_text)

root.mainloop()
