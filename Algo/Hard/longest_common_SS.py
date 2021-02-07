"""
Write a function that takes in 2 strings and returns their longest common subsequence.

A SS is a string of characters that aren't necessarily adjacent but are in order.
Of "abcd": abc, bc, ad, a, abcd, etc.

Input:
    str1 = "ZXVVYZW"
    str2 = "XKYKZPW"

Output:
    ["X", "Y", "Z", "W"]

* would levenshtein rhythm be applicable here?

answer - O(NM)T / O(NM)S --M is 2nd string
"""


def longestCommonSubsequence(str1, str2):
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
    """
    # Adding the empty space at the top allows us to
    # use something as a base case equality in the equation
    str1 = " " + str1
    str2 = " " + str2

    # Answer grid
    str_matrix = [ [None for col in range(len(str2))] for row in range(len(str1)) ]

    # Prime them--1st in row, 1st column
    for row in range(len(str_matrix)):
        str_matrix[row][0] = " "

    for col in range(len(str_matrix[0])):
        str_matrix[0][col] = " "
 
    
    # Iterate as if through a 2D matrix
    # If they equal each other, pick the left value and add r-1/c-1 (diagonal)
    for row in range(1, len(str1)):
        for col in range(1, len(str2)):
            if str1[row] == str2[col]:
                str_matrix[row][col] = str(str_matrix[row-1][col-1] + str1[row])
            else:
                left = str_matrix[row][col-1]
                up = str_matrix[row-1][col]
                if len(left) >= len(up):
                    str_matrix[row][col] = left
                else:
                    str_matrix[row][col] = up


    return list(str_matrix[-1][-1].lstrip())


if __name__ == "__main__":

    str1 = "ZXVVYZW"
    str2 = "XKYKZPW"

    print(longestCommonSubsequence(str1, str2))
