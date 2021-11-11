class Hanoi:

    def solve(self, discs):
        src = [i for i in reversed(range(1, discs+1))]
        dest = list()
        buff = list()
        self._move(discs, src, dest, buff)
        return dest

    def _move(self, discs, src, dest, buff):
        if discs:
            print(f"Disc count: {discs}")
            self._move(discs - 1, src, buff, dest)
            dest.append(src.pop())
            print(f"Num of ds: {discs}; src: {src}; buff: {buff}; dest: {dest}")
            self._move(discs - 1, buff, dest, src)


def main():
    d = Hanoi().solve(4)
    print(d)


main()
