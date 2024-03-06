import tkinter as tk
from tkinter import ttk

LEFT_SIDE_WIDTH = 0.3


def handle_click_1(event):
    frame_1.lift()


def handle_click_2(event):
    frame_2.lift()


window = tk.Tk()
window.title("Switching Frames")
window.geometry("600x400")

style = ttk.Style()
style.configure("leftside.TFrame", background="#001219")
style.configure("rightside.TFrame", background="#005f73")
style.configure("label1.TLabel", background="#540b0e", foreground="white")
style.configure("label2.TLabel", background="#e09f3e", foreground="white")
style.configure("frame1.TFrame", background="#540b0e")
style.configure("frame2.TFrame", background="#e09f3e")


left_side = ttk.Frame(window, style="leftside.TFrame")
left_side.place(relx=0, rely=0, relwidth=LEFT_SIDE_WIDTH, relheight=1)

label_1 = ttk.Label(left_side, text="Frame 01", style="label1.TLabel")
label_1.pack(expand=True, fill="both", padx=40, pady=40)
label_1.bind("<Button-1>", handle_click_1)

label_2 = ttk.Label(left_side, text="Frame 02", style="label2.TLabel")
label_2.pack(expand=True, fill="both", padx=40, pady=40)
label_2.bind("<Button-1>", handle_click_2)


right_side = ttk.Frame(window, style="rightside.TFrame")
right_side.place(
    relx=LEFT_SIDE_WIDTH, rely=0, relwidth=(1 - LEFT_SIDE_WIDTH), relheight=1
)

frame_1 = ttk.Frame(right_side, style="frame1.TFrame")
frame_1.place(relx=0, rely=0, relwidth=1, relheight=1)

frame_2 = ttk.Frame(right_side, style="frame2.TFrame")
frame_2.place(relx=0, rely=0, relwidth=1, relheight=1)

print(frame_1)
print(frame_2)

window.mainloop()
