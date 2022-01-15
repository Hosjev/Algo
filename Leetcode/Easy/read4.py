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

class File:
    def __init__(self, text):
        self.text = text
        self.seek = 0


class Solution:
    """
    Abstracted method/function to read4()
      which returns its own seek position

    Input: our file buffer? and n == number of chars to read?
    Return: file/buffer seek position (int)
    """
    def read(self, buf, n):
        """ buf: empty []; n: buffer size """
        read_idx = 0
        read_chars = 4
        local_buf = [''] * 4
        
        while read_idx < n and read_chars == 4:
            # Resetting read_chars number here in case < 4
            read_chars = read4(local_buf)
            
            for i in range(read_chars):
                if read_idx == n:
                    return read_idx
                # We fill up our own buffer, tho we don't return it 
                buf[read_idx] = local_buf[i]
                read_idx += 1
                
        return read_idx


def read4(buf):
    # MOCK API - file pointer should really be added here
    # Return # of read chars
    read_chars = 0
    try:
        local_seek = read_file.seek
    except AttributeError:
        read_file.seek = 0
        local_seek = read_file.seek
    for _ in range(len(buf)):
        if read_file.seek >= len(read_file.text):
            return read_chars
        buf[read_chars] = read_file.text[read_file.seek]
        read_chars += 1
        read_file.seek += 1
    return read_chars


read_file = File("abcdefghij")


if __name__ == "__main__":
    obj = Solution()
    n = 6
    buf = [''] * n
    seek = obj.read(buf, n)
    print(read_file.seek)
    print(buf)
