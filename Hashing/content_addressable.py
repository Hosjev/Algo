import hashlib


class File:

    def __init__(self, ifile):
        self.file = ifile

    def _open_and_hash(self):
        """Open binary, read 10M a shot, hash"""
        with open(self.file, "rb") as fh:
            f_read = fh.read(1000000)
            while f_read:
                hsh = hashlib.sha256()
                hsh.update(f_read)
                print(hsh.hexdigest())
                f_read = fh.read(1000000)


if __name__ == "__main__":
    file_to_read = "/tmp/shit"
    f = File(file_to_read)
    print(f._open_and_hash())
