"""
Given non-empty string of lowercase letters and a non-negative ints representing a key, write
function that returns new string obtained by shifting every letter to the left by "k".
Input:
    string = "xyz"
    key = 2
Output:
    "zab"

* letters should "wrap" around the alphabet. IE- if k == 2, z == b
* scramble below uses alpha indexes to gauge position to key values
* the unicode version uses unicode numbers instead
    with the caveat of returning an additional modulo that steps outside 96-122 letters
"""

def caesarCipherEncryptor(string, key):

    new_encryption = str()
    lower_alpha = 'abcdefghijklmnopqrstuvwxyz'

    def scramble(c, k):
        current_position = lower_alpha.index(c)
        d_sum = current_position + k
        new_position = (d_sum % 26)
        return lower_alpha[new_position]

    def uni_scramble(c, k):
        new_position = ord(c) + (k % 26)
        if new_position <= 122:
            return chr(new_position)
        else:
            return chr((96 + new_position) % 122)

    for x in string:
        new_encryption += uni_scramble(x, key)

    return new_encryption


if __name__ == "__main__":
    string = "yza"
    key = 57
    print(caesarCipherEncryptor(string, key))
