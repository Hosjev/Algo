import types
import selectors
import socket
import time

# Global namespace
msgs = [b"First message from client",
        b"Second message from client", b"Third message from client"]
HOST = "localhost"
PORT = 65432
select = selectors.DefaultSelector()


# Where we mock our multiple connections to the server


def start_connections(host, port, number_of_conns):
    server_address = (host, port)
    for connection_id in range(1, number_of_conns+1):
        print(f"Starting connection {connection_id} to {server_address}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_address)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(connid=connection_id,
                                     msg_total=sum(len(m) for m in msgs),
                                     recv_total=0,
                                     msgs=list(msgs),
                                     outb=b"")
        select.register(sock, events, data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    # sleeping here so I can get a look at the proc table
    # time.sleep(1)

    # process msgs sent from server (in blue)
    if mask & selectors.EVENT_READ:
        # print(f"\033[36m entering READ state \033[0m")
        recv_data = sock.recv(1024)
        # did we get data from socket
        if recv_data:
            print(
                f"\033[36m received data {repr(recv_data)} from ID {data.connid} \033[0m")
            data.recv_total += len(recv_data)
        # did we get None or our mocked msgs have reached an end
        if not recv_data or data.recv_total == data.msg_total:
            print(
                f"\033[36m closing connection to server for client {data.connid} \033[0m")
            select.unregister(sock)
            sock.close()
    # process msgs to server (in red)
    if mask & selectors.EVENT_WRITE:
        # print(f"\033[91m entering WRITE state \033[0m")
        if not data.outb and data.msgs:
            data.outb = data.msgs.pop(0)
        # and now we have data to write
        if data.outb:
            print(
                f"\033[91m sending data {repr(data.outb)} outbound from client {data.connid} \033[0m")
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]


# The mocked clients creating sockets and registered via selector
start_connections(HOST, PORT, 3)

# The main loop
try:
    while (True):
        events = select.select(timeout=1)
        if events:
            for key, mask in events:
                service_connection(key, mask)
        # Check for a socket being monitored to continue.
        if not select.get_map():
            break
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    select.close()
