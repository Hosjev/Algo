"""
Write a function that takes in 3 strings and returns a boolean representing whether the 3rd string can be formed by interweaving the 1st 2 strings.

Interweave: strings merge by alternating their letters w/o any specific pattern. For instance, the strings "abc" and "123" can be interwoven as "a1b2c3" or "abc123" or "ab1c23".

* Letters within a string must maintain their relative ordering in the woven pattern.

Input:
    one = "algoexpert"
    two = "your-dream-job"
    three = "your-algodream-expertjob"

Output:
    True

* would levenshtein rhythm be applicable here?

answer - O(NM)T / O(NM)S --M is 2nd string
"""


def interweavingStrings(str1, str2, str3):
    """
    Yes, the Levenshtein rhythm is applied but to iterate through smaller sequences
    and track them with the 2D matrix.

    Example:
        String 2 is columns
        String 1 is rows
        Dash represents my "empty" char match (longest CS)
           " " A B  D  C
        " " -  - -  -  -
         Z  -  - -  -  -
         B  -  - -B -B -B
         4  -  - -B -B -B
         C  -  - -B -B -BC

    The above DP approach or an iterative.
    -create new array with boolean values, copy of answer string
    -iterate thru one, marking off (in order) each "found" character
    -iterate thru two, same
    -if any space in new array is False, return False (this would mean a char wasn't found or in order
    -use a pointer to advance through the answer array
    -The below rhythm works for all but 1
    """
    # Sanity check
    if (len(str1) + len(str2)) != len(str3): return False

    # Now, are they present in order
    str1_answer = [False] * len(str1)
    str2_answer = [False] * len(str2)

    check_string(str1_answer, str3, str1, 0, 0)
    check_string(str2_answer, str3, str2, 0, 0)

    print(str1_answer)
    print(str2_answer)
    return False if False in str1_answer or False in str2_answer else True


def check_string(answer, str3, substring, pointer_3, pointer_i):
    while pointer_i != len(answer) and pointer_3 != len(str3):
        print(pointer_3, pointer_i)
        if str3[pointer_3] == substring[pointer_i]:
            # Advance both
            answer[pointer_i] = True
            pointer_3 += 1
            pointer_i += 1
        else:
            pointer_3 += 1


def interweavingStrings(str1, str2, str3):
    """
    Recursive solution using pointers and caching.
        -move through both str1/2 with pointers
        -those pointers reference and compare to a pointer
         in the 3rd string.
        -the recursion comes through matching each character to
         a sucessive matches in the 3rd. this is a classic DFS
         style recursion that explores ALL possible combinations of
         single-to-many character matches.
         EX--(favoring one):
             abc to def to abdecf
             a == a; and ab == ab; but c != d so we backtrack to branch "d" in 2
             d == d; de == de; f != c so we backtrack to c
    * store results in 2D matrix?
    * as for the below, where are we going to return? we must return a False branch
      and explore the next available branch. we must also return an out-of-bounds branch, as False?
    * what else are we returning? we ultimately want to return a boolean value. And if we have explored
      all possible branches, then we should return immediately a False, don't bother exploring. WASTE.
    * we only return TRUE when the last character has been matched to either 1 or 2.
    """ 
    # Same sanity check
    if (len(str1) + len(str2)) != len(str3): return False

    # B/c there are TONS of recursive calls as you DFS through potential matches,
    # a cache here will save having to re-compute the same boolean/comparison on characters
    cache = [ [None for j in range(len(two) + 1)] for i in range(len(one) + 1) ]

    return interwoven(one, two, three, 0, 0, cache)


def interwoven(one, two, three, i, j, cache):
    if cache[i][j] is not None:
        return cache[i][j]

    # K is the position of our three character
    k = i + j
    # If we've reached the end of three, we're done.
    if k == len(three):
        return True

    # As mentioned, favoring one (random)
    # so if next steps are successful, return True up the stack
    if i < len(one) and one[i] == three[k]:
        cache[i][j] = interwoven(one, two, three, i + 1, j, cache)
        if cache[i][j]:
            return True

    if j < len(two) and two[j] == three[k]:
        cache[i][j] = interwoven(one, two, three, i, j + 1, cache)
        return cache[i][j]

    cache[i][j] = False
    return False



if __name__ == "__main__":

    one = "algoexpert"
    two = "your-dream-job" # last idx 13
    three = "your-algodream-expertjob" # last idx 23

    one = "aaaa"
    two = "aaba"
    three = "aaabaaaa"

    one = "ae"
    two = "e"
    three = "see"

    #one = "aacaaaa"
    #two = "aaabaaa"
    #three = "aaaaaacbaaaaaa"


    print(interweavingStrings(one, two, three))
