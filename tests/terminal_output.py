import threading
import customtkinter as ctk
import time


def run_loop(textbox, i=0):
    if i < 100:
        print(i)
        textbox.insert("end", str(i) + "\n")
        textbox.after(
            1000, run_loop, textbox, i + 1
        )  # Schedule the next iteration after 1000ms (1 second)
    else:
        textbox.insert("end", "Loop finished\n")


def run_tkinter():
    window = ctk.CTk()
    window.title("Terminal Output")
    window.geometry("400x400")

    textbox = ctk.CTkTextbox(window)
    textbox.pack()

    run_loop(textbox)  # Pass the textbox to the run_loop function

    window.mainloop()


tkinter_thread = threading.Thread(target=run_tkinter)
tkinter_thread.start()
