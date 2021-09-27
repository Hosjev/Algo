import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 65432))

header_space = 10

while True:
    full_msg = ""
    new_msg = True

    while True:
    #Accept 16 bytes at a time
        msg = s.recv(16)
        if new_msg:
            print(f"new message length: {msg[:header_space]}")
            msglen = int(len(msg[:header_space]))
            new_msg = False

        full_msg += msg.decode("utf-8")

        if len(full_msg)-header_space == msglen:
            print(f"full msg rcvd")
            print(full_msg[header_space:])
            new_msg = True
            full_msg = ""

    print(full_msg)
