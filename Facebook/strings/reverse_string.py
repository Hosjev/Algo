class ReverseString:

    def __init__(self, s):
        self.string = s

    def eval(self):
        # NOT in-place
        pointer = len(self.string) - 1
        while pointer >= 0:
            self.string = self.string[0:pointer] + \
                          self.string[pointer + 1:] + \
                          self.string[pointer]
            pointer -= 1

        return self.string

    def eval_array(self):
        chars = [x for x in self.string]
        L = 0
        R = len(self.string) - 1
        while L < R:
            chars[L], chars[R] = chars[R], chars[L]
            L += 1
            R -= 1
        return "".join(chars)
        #return "".join(sorted(self.string, reverse=True))


def main(s):
    # ECs
    if len(s) <= 1 or len(s) == set(s):
        return s
    r = ReverseString(s).eval()
    r = ReverseString(s).eval_array()
    print(r)
    


if __name__ == "__main__":
    s = "abcdefghijkl"
    #s = "ab"
    main(s)
