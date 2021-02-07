"""
Write a function that, given a string, returns its longest palindromic substring.

A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are in themselves palindromes.

You can assume that there will only be one longest palindromic substring.

Input:
    "abaxyzzyxf"

Output:
    "xyzzyx"

* a palindrome starts when there's a duplication (0-1-2-2-1-0) or 1-2-1 pattern
* we could identify all the P's this way then eval the largest
* iterate thru every index and treat it as a possible PAL

O(n^2)T | O(n)S
"""
import time



def longestPalindromicSubstring(string):
    if len(string) > 0:
        max_palindrome = string[0]
    for idx in range(len(string)-1):
        #print("processing idx:", idx)
        max_palindrome = odd_check(idx, string, max_palindrome)
        max_palindrome = even_check(idx, idx+1, string, max_palindrome)
        #print(max_palindrome)
    return max_palindrome


def eval_max_pal(palindrome, max_pal):
    if len(palindrome) > len(max_pal):
        max_pal = palindrome
    #print("returning max:", max_pal)
    return max_pal


def odd_check(middle, string, max_palindrome):
    step = 1
    palindrome = string[middle]
    while middle-1 >= 0 and middle+step <= len(string)-1: # is this end middle+step+1?
        #print("...inside while")
        if string[middle + step] == string[middle - step]:
            palindrome = string[middle-step:middle+(step+1)]
            step += 1
        else:
            break

    return eval_max_pal(palindrome, max_palindrome)


def even_check(left, right, string, max_palindrome):
    if string[left] == string[right]:
        palindrome = string[left:right+1] # inclusive of right
    else:
        return max_palindrome

    step = 1
    while left-1 >= 0 and right+step <= len(string)-1:
        #print("...inside while r/l:", right, left, step)
        if string[right + step] == string[left - step]:
            palindrome = string[left-step:right+(step+1)]
            step += 1
        else:
            break

    return eval_max_pal(palindrome, max_palindrome)


def longestPalindromicSubstring(string):
    if len(string) == 0: return None
    elif len(string) == 1: return string[0]

    current_longest = [0, 1]

    # In this version, we look backward
    for idx in range(1, len(string)):
        odd = isPalindrome(string, idx - 1, idx - 1) 
        even = isPalindrome(string, idx - 1, idx)
        round_winner = max(odd, even, key = lambda x: x[1] - x[0])
        current_longest = max(round_winner, current_longest, key = lambda x: x[1] - x[0])

    return string[current_longest[0]:current_longest[1]]


def isPalindrome(string, left_idx, right_idx):
    while left_idx >= 0 and right_idx <= len(string):
        if string[left_idx] == string[right_idx]:
            left_idx -= 1
            right_idx += 1
        else:
            break

    # We return the last good left and right will be non-inclusive above, so we're good
    return [left_idx + 1, right_idx]



if __name__ == "__main__":

    string = "abaxyzzyxf"
    string = "it's highnoon"
    string = "aa"
    string = "fedcbaa"
    string = "abaxyzzyxf"

    print(longestPalindromicSubstring(string))
