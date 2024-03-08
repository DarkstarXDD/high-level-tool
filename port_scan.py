import socket
import threading
from queue import Queue

TARGET_IP = "192.168.1.1"
STARTING_PORT = 0
ENDING_PORT = 1023


def scan_port(port):
    try:
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_socket.connect((TARGET_IP, port))
        return True

    except:
        return False


for port in range(STARTING_PORT, ENDING_PORT):
    port_status = scan_port(port)

    if port_status:
        print(f"Port {port} is open!")
    else:
        print(f"Port {port} is closed!")
