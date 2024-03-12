import sidebar
import sidebarButton as sb
import currentFrame
import portScannerFrame

import customtkinter as ctk


class RunApp:
    def __init__(self):

        window = ctk.CTk()
        window.title("High Level Tool")
        window.geometry("1400x650")

        sidebar_frame = sidebar.Sidebar(window)
        current_frame = currentFrame.CurrentFrame(window)

        # Frames
        portscan_frame = portScannerFrame.PortScannerFrame(current_frame)

        # Sidebar Buttons
        sb_button_port = sb.SidebarButton(sidebar_frame, "Port Scanner", portscan_frame)

        window.mainloop()


runapp = RunApp()
