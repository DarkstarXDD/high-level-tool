import tkinter as tk


def label_clicked(event):
    print("Label clicked!")


window = tk.Tk()
window.title("Clickable Label Example")
window.geometry("300x200")

label = tk.Label(
    window, text="Click me!", font=("Arial", 12), bg="lightgray", padx=10, pady=5
)
label.pack(pady=20)

# Bind the <Button-1> event to the label_clicked function
label.bind("<ButtonRelease-1>", label_clicked)

window.mainloop()
