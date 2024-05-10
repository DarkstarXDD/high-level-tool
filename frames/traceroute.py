import subprocess
import threading

import customtkinter as ctk


class TracerouteFrame(ctk.CTkFrame):
    def __init__(self, parent, hover, tooltips, descriptions):
        super().__init__(parent)

        self.running = False

        self.poppins_200 = ctk.CTkFont(family="Poppins", size=14)
        self.poppins_300 = ctk.CTkFont(family="Poppins Medium", size=14)
        self.poppins_400 = ctk.CTkFont(family="Poppins SemiBold", size=18)
        self.cascadia_200 = ctk.CTkFont(family="Cascadia Mono", size=14)

        self.configure(corner_radius=0, fg_color="#242424")
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.columnconfigure(0, weight=1, uniform="a")
        self.rowconfigure(0, weight=4, uniform="a")
        self.rowconfigure(1, weight=6, uniform="a")
        self.rowconfigure(2, weight=3, uniform="a")

        # ------------------------ 3 Frames for the Sections -----------------------
        frame_top = ctk.CTkFrame(self)
        frame_top.grid(row=0, sticky="nesw", padx=10, pady=(10, 5))

        frame_top.columnconfigure(0, weight=1, uniform="a")
        frame_top.columnconfigure(1, weight=2, uniform="a")
        frame_top.columnconfigure(2, weight=2, uniform="a")
        frame_top.rowconfigure((0, 1, 2), weight=1, uniform="a")

        frame_middle = ctk.CTkFrame(self)
        frame_middle.grid(row=1, sticky="nesw", padx=10, pady=5)
        frame_middle.configure(fg_color="#242424")

        frame_bottom = ctk.CTkFrame(self)
        frame_bottom.grid(row=2, sticky="nesw", padx=10, pady=(5, 10))
        frame_bottom.configure(fg_color="#242424")

        # -------------------------------- Labels --------------------------------
        label_target = ctk.CTkLabel(frame_top, text="Destination IP", anchor="w")
        label_target.configure(font=self.poppins_200)
        label_target.grid(row=0, column=0, sticky="nesw", padx=15, pady=5)

        label_target.bind(
            "<Enter>", lambda event: hover.display(tooltips["traceroute"])
        )
        label_target.bind("<Leave>", lambda event: hover.display(""))

        # -------------------------------- Inputs --------------------------------
        self.input_target = ctk.CTkEntry(frame_top)
        self.input_target.insert(0, "192.168.1.1")
        self.input_target.grid(row=0, column=1, sticky="nesw", padx=5, pady=5)

        # -------------------------------- Buttons --------------------------------
        self.button_reset = ctk.CTkButton(frame_top)
        self.button_reset.configure(
            text="Reset",
            font=self.poppins_400,
            command=self.handle_reset_click,
        )
        self.button_reset.grid(row=0, column=2, sticky="nesw", padx=(100, 10), pady=5)

        self.button_start = ctk.CTkButton(frame_top)
        self.button_start.configure(
            text="Run Tracert Command",
            font=self.poppins_400,
            fg_color="#314724",
            hover_color="#26361B",
            command=self.handle_start_click,
        )
        self.button_start.grid(row=1, column=2, sticky="nesw", padx=(100, 10), pady=5)

        self.button_cancel = ctk.CTkButton(frame_top)
        self.button_cancel.configure(
            text="Cancel",
            font=self.poppins_400,
            fg_color="#70292A",
            hover_color="#592122",
            state="disabled",
            command=self.handle_cancel_click,
        )
        self.button_cancel.grid(row=2, column=2, sticky="nesw", padx=(100, 10), pady=5)

        # ----------------------------- Main Output ------------------------------
        self.main_output = ctk.CTkTextbox(frame_middle, font=self.cascadia_200)
        self.main_output.pack(expand=True, fill="both")

        # ------------------------------ Description -----------------------------
        txtbox_description = ctk.CTkTextbox(frame_bottom, font=self.poppins_200)
        txtbox_description.insert("end", descriptions["traceroute_command"])
        txtbox_description.configure(fg_color="#2b2b2b", state="disabled")
        txtbox_description.pack(expand=True, fill="both")

    def run_tracert(self):
        self.running = True
        target = self.input_target.get()
        self.main_output.delete("1.0", "end")

        try:
            tracert_process = subprocess.Popen(
                ["tracert", target],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
                text=True,
            )

            # Read and print output line by line
            for line in iter(tracert_process.stdout.readline, ""):
                if not self.running:  # Check if Cancel button is clicked
                    tracert_process.kill()  # Terminate the process
                    print("Tracert command execution was interrupted!")
                    self.main_output.insert(
                        "end", "\nTracert command execution was interrupted!"
                    )
                    break
                print(line, end="")
                self.main_output.insert("end", line)

            # Read and print error line by line, if there is any.
            for line in iter(tracert_process.stderr.readline, ""):
                print(line, end="")
                self.main_output.insert("end", line)

        except Exception as error:
            print("An error occurred:", error)
            self.main_output.insert("end", error)

        if self.running:
            self.main_output.insert("end", "\nTracert command execution is done!")

        self.button_start.configure(state="normal")
        self.button_reset.configure(state="normal")
        self.button_cancel.configure(state="disabled")

    def handle_cancel_click(self):
        self.running = False

    def handle_reset_click(self):
        self.main_output.delete("1.0", "end")
        self.input_target.delete(0, "end")
        self.input_target.insert(0, "192.168.1.1")

    def handle_start_click(self):
        self.button_start.configure(state="disabled")
        self.button_reset.configure(state="disabled")
        self.button_cancel.configure(state="normal")
        threading.Thread(target=self.run_tracert).start()
