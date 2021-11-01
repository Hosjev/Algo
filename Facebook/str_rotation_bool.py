class Rotation:

    def is_substring(self, p, s):
        return p in s

    def is_rotation(self, p, s):
        if (not p or not s) or \
           (len(p) != len(s)):
            return False
        return self.is_substring(p, (s + s))

def main(p, s):
   a = Rotation().is_rotation(p, s) 
   print(a)


p = "abc"
s = "cab"
main(p, s)
