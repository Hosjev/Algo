"""
Write a function that takes in a string and returns the longest substring (contiguous) w/o any duplicate characters.

Input:
    str = "clementisacap"

Output:
    "mentisac"

answer - O(NM)T / O(NM)S --M is 2nd string
"""


def longestSubstringWithoutDuplication(string):
    """
    Algo version:
        -create empty hash table
        -this hash table will store unique characters and track their index
        -create solution string and store result (longest) here
        -track "start" of new non-dup strings with "pointer"
    """
    pointer_idx = 0
    result = string[0]
    character_hash = {}
    character_hash[string[0]] = 0

    for idx in range(1, len(string)):
        if string[idx] in character_hash.keys():
            # Advance pointer by referencing ME/idx
            pointer_idx = max(pointer_idx, character_hash[string[idx]] + 1)
            # Update hash table with new index
            character_hash[string[idx]] = idx
        else:
            # Store index
            character_hash[string[idx]] = idx

        current_result_length = len(result)
        new_result = string[pointer_idx:idx + 1]
        new_result_length = len(new_result)
        if new_result_length > current_result_length:
            result = new_result

    return result


if __name__ == "__main__":

    string = "clementisacap"
    #string = "abcb"
    string = "abcdeabcdefc"
    # Algo: abcdef
    # Me:   abcdefc

    print(longestSubstringWithoutDuplication(string))
