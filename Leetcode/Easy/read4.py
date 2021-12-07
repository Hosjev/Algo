"""
Abstracted: read4
            Let's say our file contains "abcdefghij"
            -1st four will be "abcd"
            -buf4 is filled with those chars
            -pointer will remain at "e"
            -read_chars keeps track of pointer place
            -we move our own pointer "read_idx" along w/buf4
            -from below read, we return location of seek
"""
class Solution:
    """ Abstracted method/function read4() returns 4 chars at a time """
    def read(self, buf, n):
        """ buf: empty []; n: buffer size """
        read_idx = 0
        read_chars = 4
        
        buf4 = [''] * 4
        
        while read_idx < n and read_chars == 4:
            # Resetting read_chars number here in case < 4
            read_chars = read4(buf4)
            
            for i in range(read_chars):
                if read_idx == n:
                    return read_idx
                
                buf[read_idx] = buf4[i]
                read_idx += 1
                
        return read_idx
