from pathlib import Path
import argparse

class DirContents:
    def __init__(self, dir_name):
        self.dir_name = dir_name

    def cwd(self):
        for fpath in Path.cwd().rglob("*"):
            print(f"directory: {fpath}")

    def tree(self):
        print(f"top level\n + {self.dir_name}")
        for subpath in sorted(self.dir_name.rglob("*")):
            # relative depth
            depth = len(subpath.relative_to(self.dir_name).parts)
            spacer = "    " * depth
            print(f"{spacer}+ {subpath.name}")


if __name__ == "__main__":
    # Do argparse next
    parser = argparse.ArgumentParser(description="display directory contents")
    parser.add_argument("--dir")
    args = parser.parse_args()

    if not args.dir:
        dobj = DirContents(Path("/home/hosjev/PythonPlay/IO"))
    else: dobj = DirContents(Path(args.dir))
    dobj.tree()
