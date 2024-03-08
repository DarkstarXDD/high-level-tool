import socket

client_hostname = socket.gethostname()
ipv4 = socket.gethostbyname(client_hostname)

print(ipv4)
print(client_hostname)
