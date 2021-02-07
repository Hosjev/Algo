"""
We have 2 strings. The 1st is a pattern consisting only of "x" and "y"s'. The 2nd is a normal string of alphanumeric. Write a function that checks whether the pattern is present in the 2nd string.

A string S0 is said to match a pattern if replacing all "x"s in the pattern with some non-empty substring S1 of S0 and replacing all "y"s in the pattern with some non-empty substring S2 of S0 yields the same string S0.

If the string doesn't match the pattern, function should return an empty array. Otherwise, return an array holding the strings S1 and S2 that rep "x" and "y". In that order. If the pattern doesn't contain "x" or "y", the respective letter should be represented in the final array you return.

You can assume there will never be more than one pair of strings S1 and S2 that appropriately match "x" and "y". (if there's a match, they'll be one pattern)

Input:
    pattern = "xxyxxy"
    string = "gogopowerrangergogopowerranger"

Output:
    "_test_this is a _testtest_ to see if _testestest_ it works"

answer - O(NM)T / O(NM)S --M is 2nd string
"""
import time


def patternMatcher(string, pattern):
    """
    The steps would be:
        -identify if you're looking for 1 or 2 "things"
        -(Algo add) normalize "x" and "y". IE-if your pattern starts w/y, turn to x (or simply swap)
        -find 1st pattern (x or y)
        --using find, identify the whole thing with a progressively hungry 1 to many char
          match. if (the number of times x or y is present in pattern) matches the find, cont.
        --if we can't get an exact match-to-match #, immediately exit w/empty array
        -find 2nd pattern in same manner (this would be done with slices)
        -next check: do individual slices from 2 substrings (or 1) match
        -then iterate straight through with x == patt 1 and y == patt 2
        -if you can get all the way thru, exit with x = patt, y = patt
    """
    if len(pattern) > len(string):
        return []

    new_pattern = normalize_pattern(pattern)
    is_swapped = new_pattern[0] != pattern[0]
    counts = {"x": 0, "y": 0}
    first_y_pos = get_counts_and_first_y_pos(new_pattern, counts)
    if counts["y"] != 0:
        for len_of_x in range(1, len(string)):
            len_of_y = (len(string) - len_of_x * counts["x"]) / counts["y"]
            if len_of_y <= 0 or len_of_y % 1 != 0:
                continue
            len_of_y = int(len_of_y)
            y_idx = first_y_pos * len_of_x
            x = string[:len_of_x]
            y = string[y_idx: y_idx + len_of_y]
            potential_match = map(lambda char: x if char == "x" else y, new_pattern)
            if string == "".join(potential_match):
                return [x, y] if not is_swapped else [y, x]
    else: # NO Y's
        len_of_x = len(string) / counts["x"]
        if len_of_x % 1 == 0:
            len_of_x = int(len_of_x)
            x = string[:len_of_x]
            potential_match = map(lambda char: x, new_pattern)
            if string == "".join(potential_match):
                return [x, ""] if not is_swapped else ["", x]

    return [] # A final return if something goes bad


def get_counts_and_first_y_pos(pattern, counts):
    first_y_pos = None
    for i, char in enumerate(pattern):
        counts[char] += 1
        if char == "y" and first_y_pos is None:
            first_y_pos = i
    return first_y_pos


def normalize_pattern(pattern):
    pattern_chars = list(pattern)
    if pattern[0] == "x":
        return pattern_chars
    else:
        return list(map(lambda char: "x" if char == "y" else "y", pattern_chars))




if __name__ == "__main__":

    pattern = "xxyxxy"
    string = "gogopowerrangergogopowerranger"

    print(patternMatcher(string, pattern))
