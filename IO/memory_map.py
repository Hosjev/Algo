import mmap
import time
import os

def pure_mem_io():
    m_buffer = mmap.mmap(-1, length=100, access=mmap.ACCESS_WRITE)
    pid = os.fork()
    if pid == 0:
        m_buffer[0:100] = b"b" * 100
    else:
        # do something
        time.sleep(1)
        print(m_buffer[0:100].decode())


pure_mem_io()
