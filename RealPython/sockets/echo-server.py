import socket

HOST = "localhost"
PORT = 65432

# The WITH statement below acts like Java's try-with-resources
# --the close() call is made automatically
# --AF_INET == IPV4
# --SOCK_STREAM == TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()
    # Same with the incoming connection/socket
    # --we close() when out of WITH
    with connection:
        print(f"Connection made by: {address}")
        while True:
            data = connection.recv(1024)
            if not data:
                print(f"...end of transmission from {address}")
                break
            connection.sendall(data)
