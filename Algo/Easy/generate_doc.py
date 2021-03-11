"""
Given set of characters and string repping doc you need to generate. Write function that returns boolean whether you can generate doc based on characters.


Input:
    chars = "tt  ghrsxtepEi!oeB leAs"
    docu = "AlgoExpert is the Best!"
Output:
    true


** "" empty string is always true
** you can only use a single char once
"""
import time


def generateDocument(characters, document):
    # Write your code here.
    # this seems terribly easy
    # what am I missing?
    # create a queue? pop them off as used
    # listify them, mark as used
    # immediately return when 1st failure
    # unshuffle chars and treat as palindrome?

    # create stack
    stack = list(characters)

    idx = 0
    while (idx < len(document)):
        current_char = document[idx]
        # print(idx, current_char)
        if current_char in stack:
            idx += 1
            stack.remove(current_char)
        else:
            return False

    return True


chars = "tt  ghrsxtepEi!oeB leAs"
docu = "AlgoExpert is the Best!"

print(generateDocument(chars, docu))
