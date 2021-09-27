def longest_palindrome(s):
    """
    1. define helper to determine if palindrome
       a. this helper must take odd or even centers
    2. define edge case early -- if len of s <= 1, ret s
    3. run through each character and do odd/even check
    4. record max answer, return string
    """

    if len(s) <= 1:
        return s

    max_length = 1
    substring = s[0]

    # We start with the understanding that [0] is already 1
    for idx in range(len(s)):
        # Run odd
        S, E = palindrome_helper(s, idx - 1, idx + 1)
        # Eval odd
        max_length, substring = eval_max(S, E, s, substring, max_length)
        # Run even
        S, E = palindrome_helper(s, idx, idx + 1)
        # Eval even
        max_length, substring = eval_max(S, E, s, substring, max_length)

    return substring


def eval_max(S, E, s, substring, max_length):
    """ Eval max and substring from start and end points """
    if (E - S) + 1 > max_length:
        substring = s[S:E + 1]
        max_length = (E - S) + 1
    return max_length, substring


def palindrome_helper(s, left, right):
    if (left < 0) or (right > len(s) - 1):
        return left + 1, right - 1

    # Eval l/r
    if s[left] == s[right]:
        return palindrome_helper(s, left - 1, right + 1)
    else:
        return left + 1, right -1


def is_palindrome(substring, left, right):
    if (right-left) <= 0:
        return True

    if substring[left] == substring[right]:
        return is_palindrome(substring, left+1, right-1)
    else:
        return False


s = "ebabbabv"
#s = "bab"
#s = "ebababv"
#s = "bb"

print(longest_palindrome(s))
