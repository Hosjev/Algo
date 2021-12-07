from multiprocessing import Process
from multiprocessing import shared_memory
from multiprocessing import Array
# < 3.8 has pretty limited and weird looking array/vals/obj shm implementation

def modify(buf_name):
    shm = shared_memory.SharedMemory(buf_name)
    shm.buf[0:50] = b"b" * 50
    shm.close()

if __name__ == "__main__":
    shm = shared_memory.SharedMemory(create=True, size=100)

    try:
        shm.buf[0:100] = b"a" * 100
        proc = Process(target=modify, args=(shm.name,))
        proc.start()
        proc.join()
        print(bytes(shm.buf[:100]))
    finally:
        shm.close()
        shm.unlink()
