import socket
import threading
import queue

TARGET_IP = "192.168.1.1"
STARTING_PORT = 0
ENDING_PORT = 100

open_ports = []
new_queue = queue.Queue()


def scan_port(port):
    try:
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_socket.settimeout(1)
        new_socket.connect((TARGET_IP, port))
        new_socket.close()
        return True

    except:
        return False


def fill_queue(port_list):
    for port in port_list:
        new_queue.put(port)


def worker():
    while not new_queue.empty():
        port = new_queue.get()

        if scan_port(port):
            print(f"Port {port} is open!")
            open_ports.append(port)


# Create the port list & add the ports to the queue
port_list = range(STARTING_PORT, ENDING_PORT)
fill_queue(port_list)


# Create the thread list
thread_list = []

for t in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()
