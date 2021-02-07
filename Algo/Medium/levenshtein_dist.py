"""
Write a function that takes in 2 strings and returns the minimum number of edit
operations that need to be performed on the 1st string to get to the 2nd string.

Input:
    str1 = "abc"
    str2 = "yabd"
Output:
    2 # insert y; substitute "c" for "d"

* strings
* 3 operations that count: insertion, deletion, substitution
answer - O(N*m)T O(N*m)S --N=nodes, d=depth
"""


def levenshteinDistance(str1, target):
    # This is essentially averaging changes as they move through the grid
    # Sanity check
    if len(target) == 0 and len(str1) == 0: return 0

    # Build the array to store minimum changes: str1 rows x target cols
    array = [ [0 for c in range(len(target)+1)] for r in range(len(str1)+1) ]

    # Prime array with answers given an empty start string
    # Row 0 Col 0 = 0; R0-Cend = str1R-str2end; R1-end-C0 = str1R1-end-str20
    for col in range(1, len(target)+1):
        array[0][col] = col
    for row in range(1, len(str1)+1):
        array[row][0] = row

    # Now we can execute a formula
    # Columns = target
    # Our empty strings are both worst case scenario and base case
    # 1st ex-yabd
    #  ""  y  a  b  d
    # [[0, 1, 2, 3, 4], ""
    #  [1, 0, 0, 0, 0], a
    #  [2, 0, 0, 0, 0], b
    #  [3, 0, 0, 0, 0]] c
    # The rhythm starts after the priming in 1
    for R in range(1, len(str1)+1): # Inclusive of last grid
        for C in range(1, len(target)+1):
            # Unfortunately, we start at index 0 in strings
            if str1[R-1] == target[C-1]:
                array[R][C] = array[R-1][C-1]
            else:
                # Set to lowest average of the 3 adjacent corners PLUS my edit
                #                 min(left,           diagonal,          up)
                array[R][C] = 1 + min(array[R][C-1], array[R-1][C-1], array[R-1][C])

    return array[-1][-1]


if __name__ == "__main__":

    str1 = "abc"
    target = "yabd"
    str1 = "algoexpert"
    target = "algozexpert"


    print(levenshteinDistance(str1, target))
