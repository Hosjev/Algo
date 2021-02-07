import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

header_space = 10

while True:
    clientsocket, address = s.accept()
    print(f"Connection made from {address}")

    msg = "You've connected to my server."
    msg = f"{len(msg):<{header_space}}{msg}"

    clientsocket.send(bytes(msg, "utf-8"))
    clientsocket.close()
