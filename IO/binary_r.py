import argparse

from pathlib import Path


class IO:
    def __init__(self, file_name):
        """ Not a context manager. Class w/methods to call 'open'. """
        self.file_name = file_name

    def read_png(self):
        with open(self.file_name, "rb") as fh:
            print(fh.readline())



if __name__ == "__main__":

    # Read a binary file
    parser = argparse.ArgumentParser(description="Read binary files")
    parser.add_argument("--infile", help="input file")
    args = parser.parse_args()
    infile = Path.cwd().joinpath("Input", args.infile)

    fobj = IO(str(infile))
    fobj.read_png()
