""" The pipes here are os.pipe(), os.write() and os.fdopen() """
import os
import time

r, w = os.pipe()

# This script
parent = os.getpid()
# This return is actually the PID of child 
pid = os.fork()


if pid > 0:
    # PARENT
    # close read channel
    #os.close(r)
    print("Hello from parent at PID: ", parent)
    msg = b"...writing to channel for child"
    os.write(w, msg)
    print("Sent msg:", msg.decode())
else:
    # CHILD
    # close write channel
    os.close(w)
    print("Hello from child at forked PID and new PID:", pid, os.getpid())
    msg = os.fdopen(r)
    print("Child reading from channel:", msg.read())
