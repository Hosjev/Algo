class StringPerm:

    def __init__(self, string, perm):
        """ Input: 2 strs; Output: bool """
        self.string = string
        self.perm = perm

    def edge_cases(self):
        if len(self.string) != len(perm) or \
          not self.string or not self.perm:
            return False

    def brute_force(self):
        return sorted(self.string) == sorted(self.perm)

    def mapping(self):
        # Map string1
        ascii_map = dict()
        for i in self.string:
            try:
                ascii_map[i] += 1
            except KeyError:
                ascii_map[i] = 1
        return ascii_map

    def check_permutation(self):
        ascii_map = self.mapping()
        for i in self.perm:
            try:
                if not self.perm.count(i) == ascii_map[i]:
                    return False
            except KeyError:
                return False
        return True


def main(s, p):
    print(StringPerm(s, p).check_permutation())


if __name__ == "__main__":
    s = "nib"
    p = "inx"
    main(s, p)
