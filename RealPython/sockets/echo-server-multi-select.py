import selectors
import types
import socket

HOST = "localhost"
PORT = 65432


# Global args and setup
select = selectors.DefaultSelector()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print(f"Server listening on: {HOST} | {PORT}")
lsock.setblocking(False)
select.register(lsock, selectors.EVENT_READ, data=None)


# This is our handler for server socket (data=None)
def accept_wrapper(sock):
    connection, address = sock.accept()
    print(f"Connection accepted from: {connection}")
    connection.setblocking(False)
    data = types.SimpleNamespace(addr=address, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    select.register(connection, events, data=data)


# This is our handler for client-side connections
def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb += recv_data
        else:
            print(
                f"\033[91m no more data to read from client, closing connection w/: {data.addr} \033[0m")
            select.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"\033[36m echoing {repr(data.outb)} to {data.addr} \033[0m")
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]


# The server event loop
try:
    while (True):
        events = select.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting...")
finally:
    select.close()
