import socket

HOST = "localhost"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Im saying hello from the client')
    data = s.recv(1024)

print(f"socket closed and received data from server: {data}")
