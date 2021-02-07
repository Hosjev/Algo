"""
Write a function that takes in a big string and an array of smaller strings. Return an array (equal length of smaller) contained booleans indicating whether that smaller string is in the bigger string.

* don't use any built-in string methods

Input:
    big = "this is a big string"
    small_strings = ["this", "yo", "is", "a", "bigger", "string"]

Output:
    [True, False, True, True, False, True, False]

answer - O(NM)T / O(NM)S --M is 2nd string
"""
import time


def multiStringSearch(big, smalls):
    """
    The steps would be:
        -create answer array from smalls (all False/default)
        -create cache of letters from big -- key-unique letter: value-index List
        -use pointer at small array before entering while
    """
    answer = [False] * len(smalls)

    cache = {}
    for i in range(len(big)):
        if big[i] not in cache.keys():
            cache[big[i]] = [i]
        else:
            cache[big[i]].append(i)

    s_idx = 0
    while s_idx < len(smalls):
        first_char = smalls[s_idx][0]
        #time.sleep(.2)
        #print(first_char)
        try:
            indices = cache[first_char]
        except KeyError:
            s_idx += 1
            continue
        for idx in indices:
            end_idx = idx + len(smalls[s_idx])
            if big[idx: end_idx] == smalls[s_idx]:
                answer[s_idx] = True
        # Matches have been made (or not), advance regardless
        s_idx += 1

    return answer


def algoMultiStringSearch():
    # Using a suffix trie from big
    # iterate through smalls and reviewing trie
    pass
    

if __name__ == "__main__":

    big = "this is a big string"
    big = "abcdefghijklmnopqrstuvwxyz"
    small_strings = ["this", "yo", "is", "a", "bigger", "string"]
    small_strings = ["abc", "mnopqr", "wyz", "no", "e", "tuuv"]

    print(multiStringSearch(big, small_strings))
