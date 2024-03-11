import threading
import customtkinter as ctk
import time


def run_loop():
    for i in range(0, 100):
        print(i)
        time.sleep(1)


def run_tkinter():
    window = ctk.CTk()
    window.title("Terminal Output")
    window.geometry("400x400")

    textbox = ctk.CTkTextbox(window)
    textbox.insert("0.0", "Testing")
    textbox.pack()

    window.mainloop()


loop_thread = threading.Thread(target=run_loop)
tkinter_thread = threading.Thread(target=run_tkinter)

loop_thread.start()
tkinter_thread.start()
