"""
Given a non-empty array of arrays where each triad represents a disk. The #'s represent: width, depth, height. Stack up the disks to maximize the height of the stack. A disk must have a strictly smaller width, depth and height than any below it.

Your function should return an array of the disks in the final stack, starting with the top disk and ending with the bottom disk. Note that you can't rotate disks; in other wods, the ints in each subarray must be [width, depth, height] at all times.

Input:
    pi = "3141592653589793238462643383279"
    numbers = [
        "314159265358979323846",
        "26433",
        "8",
        "3279",
        "314159265",
        "35897932384626433832",
        "79"
        ]

Output:
    2 # "314159265, 35897932384626433832, 79"

answer - O(N^2)T O(N)S
"""

def numbersInPi(pi, numbers):
    """
    Using hash table to store numbers array
        1-build hash table--key=starting sequence from numbers array, value=whole seq
        2-from the hash keys, build list of potential starts (=3)
        3-iterate through potential starts
    init max count at infinity
    character == [-1] (we start w/3)
    iterate through hash table keys
    if key == char, subarray = value in hash
    if subarray == pi[char:len(subarray)]: add to count (min)
    * you don't need starting potentials, you'll just iterate through keys for that
      first match until char exceeds len of pi
    * scratch that, I do need to know when to stop
      it's "for x in starts: while ..."
      what do we do if we fail on start?

    Algo version (DP):
        create hash table that instead stores every prefix (or suffix) of pi
        the value ends up being the minumum # of spaces this prefix contains
        this value is arrived at by seeing if the prefix is in the numbers array
        if "2" is in the array, then its (suffix) val is 0.
        if "92" is in the array, its val is 0
        if "9" and "2" are in the array, that val is 0+1
        this becomes about min'ing the prefixes (or suffixes)

    """
    pi_matches = numbers
    cache = {}
    spaces = recur_pi(pi, pi_matches, cache, 0)

    print(f"Pi:", pi)
    print(f"matches:", pi_matches)
    print(f"cache:", cache)
    print(f"spaces:", spaces)
    return -1 if spaces == float("inf") else spaces


def recur_pi(pi, pi_matches, cache, idx):
    """
    Pi is my original string.
    pi_matches is my hash of numbers.
    cache is where I store individual indices to keep track of mins
    idx is my index moving foward into suffixes

    """
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]

    spaces = float("inf")

    for x in range(idx, len(pi)):
        prefix = pi[idx:x + 1]
        if prefix in pi_matches:
            min_in_suffix = recur_pi(pi, pi_matches, cache, x + 1)
            spaces = min(spaces, min_in_suffix + 1)

    cache[idx] = spaces
    return cache[idx]



if __name__ == "__main__":

    pi = "3141592653589793238462643383279"
    numbers = [
        "314159265358979323846",
        "26433",
        "8",
        "3279",
        "314159265",
        "35897932384626433832",
        "79"
        ]

    print(numbersInPi(pi, numbers))
