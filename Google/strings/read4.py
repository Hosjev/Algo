# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self._set_local()

    def _set_local(self, cr=0):
        self.fp = 0
        self.local_buf = [''] * 4
        self.chars_read = read4(self.local_buf) + cr

    def read(self, buf: List[str], n: int) -> int:
        """Take in empty buffer and number of chars to read.
           Keep local buffer as full as possible.
           Keep track of seek position with local object FP.
           Refill when fp reaches 4.
           Offset self.chars_read when inside loop.
           Return local chars_read.
        """
        chars_read = 0
        if self.fp == 4: self._set_local()

        # seek tracks read, chars accounts for possible null
        while self.chars_read > 0:
            if self.fp == 4: self._set_local(chars_read)
            buf[chars_read] = self.local_buf[self.fp]
            self.fp += 1
            chars_read += 1
            if chars_read == n:
                self.chars_read -= chars_read
                return chars_read

        return chars_read


if __name__ == "__main__":
    # Read4 api returns num of actual chars read
    #Input: file = "abc", queries = [1,2,1]
    #Output: [1,2,0]
    #Explanation: The test case represents the following scenario:
    #File file("abc");
    #Solution sol;
    #sol.read(buf, 1) read "a" into buffer, pointer advanced by 1, return 1 char read
    #sol.read(buf, 2) read "bc" into buffer, pointer advanced by 2, return 2 char read
    #sol.read(buf, 1) pointer (seek) has already reached EOF, ret 0 char read
    #File file("abcdefg");
    #Solution sol;
    #sol.read(buf, 2) ab,2,fp2
    #sol.read(buf, 1) c,1,fp3
    #sol.read(buf, 2) d,2,fp4 --reset lbuf efg
    #File file("abcde");
    #Solution sol;
    #sol.read(buf, 4) a,fp1,cr1;b,fp2,cr2;c,fp3,cr3;d,fp4,cr4 --> self.cr -= 4
    #sol.read(buf, 1)
    #sol.read(buf, 1)
