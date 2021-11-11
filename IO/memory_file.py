import mmap

def mmap_io(in_file):
    with open(in_file, "r") as fd:
        with mmap.mmap(fd.fileno(), length=0, access=mmap.ACCESS_READ) as fd_mmap:
            print(fd_mmap.read().decode())


mmap_io("/home/wendiw/Xenial/PythonPlay/README.md")
mmap_io("/tmp/Xorg.crouton.1.log")
