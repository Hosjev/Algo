import socket

HOST = "localhost"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for i in range(1,100):
        msg = f"I am saying hello from client, msg: {i}".encode()
        s.sendall(msg)
        data = s.recv(1024)
        print(data.decode())

# TODO: add input from user to send (just receive echo)
print(f"socket closed to server")
