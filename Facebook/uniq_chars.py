class Uniqueness:

    def eval(self, s):
        if not s: return True
        hash_chars = dict()
        for i in s:
            try:
                if hash_chars[i]:
                    return False
            except KeyError:
                hash_chars[i] = 1
        return True

def main(s):
    print(Uniqueness().eval(s))


s = "abcdeff"
main(s)
