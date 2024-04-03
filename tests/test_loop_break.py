import socket


def port_scan(target, start_port, end_port):
    print(f"Scanning target {target}...")
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a timeout for connection attempt
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()
        except KeyboardInterrupt:
            print("Scan interrupted by user.")
            break  # Break out of the loop if user interrupts
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    target = input("Enter target IP address: ")
    start_port = int(input("Enter starting port number: "))
    end_port = int(input("Enter ending port number: "))
    port_scan(target, start_port, end_port)
