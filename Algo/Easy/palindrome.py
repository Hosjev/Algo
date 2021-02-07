"""
Write function that takes a non-empty string and returns a bool answer to a palindrome. 
Input:
    string = "abcdcba"
Output:
    True

* a string is immutable but indexable
* watch TSC here
* turn into array and keep eliminating 0 and -1?
  as soon as a match fails, return False
"""

def isPalindrome(string):
    # Could easily just use string
    def inner_palindrome(l, r):
        # We reached a single or double middle w/o failing
        if (l + abs(r)) >= len(string):
            return True

        #left = str_array[l]
        #right = str_array[r]
        left = string[l]
        right = string[r]
        if left != right:
            return False
        return inner_palindrome(l+1, r-1)

    str_array = [x for x in string]

    return inner_palindrome(0, -1)


if __name__ == "__main__":
    string = "abcdcba"
    fstring = "acdcba"
    print(isPalindrome(string))
