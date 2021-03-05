import os

r, w = os.pipe()

pid = os.fork()

if (pid > 0):
    # PARENT
    # close read channel
    os.close(r)
    print("Hello from parent at PID: ", pid)
    msg = b"...writing to channel for child"
    os.write(w, msg)
    print("Sent msg:", msg.decode())

else:
    # CHILD
    # close write channel
    os.close(w)
    print("Hello from child at PID:", pid)
    msg = os.fdopen(r)
    print("Child reading from channel:", msg.read())
