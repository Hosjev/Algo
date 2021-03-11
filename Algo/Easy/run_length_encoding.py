"""
Given head of singly-linked list whose nodes are in order. Write function that returns same object with no DUPS.
Alter in place.

Input:
    string = "AAAAAAAAAAAABBCCCCDD"
Output:
    "9A4A2B4C2D"

"""
import time


def runLengthEncoding(string):
    # Write your code here.
    # AABBCC -6
    def _inner_recur(idx, char_match, count, answer):
        # exit if idx beyond scope of string
        if ((idx) == len(string)):
            answer += str(count) + char_match
            return answer

        char = string[idx]
        # print(idx, char_match, count, char)
        # if we reach 9 for any character, start over
        if count == 9:
            answer += str(count) + char_match
            count = 1
        elif char == char_match:
            count += 1
        else:
            answer += str(count) + char_match
            count = 1

        return _inner_recur(idx + 1, char, count, answer)

    return _inner_recur(1, string[0], 1, "")


string = "AAAAAAAAAAAABBCCCCDDZ"
# string = "AABBCC"
print(runLengthEncoding(string))
