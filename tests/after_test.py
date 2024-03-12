import tkinter as tk


def update_frame(frame, counter):
    # Update the frame content
    label.config(text="Counter: " + str(counter))
    # Schedule the next update after 100 milliseconds
    frame.after(1000, update_frame, frame, counter + 1)


root = tk.Tk()
root.title("Update Specific Frame Example")

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Counter: 0")
label.pack()

# Start updating the frame
update_frame(frame, 0)

root.mainloop()
