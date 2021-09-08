import argparse
from pathlib import Path


class ContextIO():
    """ Overwriting "with" """
    def __init__(self, path):
        self.__path = path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

    def __iter__(self):
        return self

    def __next__(self):
        init_data = self.__file_object.read(4)
        if self.__file_object is None:
            raise StopIteration
        else:
            data = self.__file_object.read(4)
            return data



def display_contents(reader, file_name):
    with reader(file_name) as fh:
        for line in fh:
            print(line)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Test file I/O with context class")
    parser.add_argument("--infile", type=str, help="file to read")
    args = parser.parse_args()

    # Read a file
    infile = str(Path.cwd().joinpath("Input", args.infile))
    #display_contents(f_obj, infile)
    # This does not work as I don't have the correct IO calls
    content = ""
    with ContextIO(infile) as fh:
        for i in fh:
            content += i
