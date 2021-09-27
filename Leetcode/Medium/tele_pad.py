DIGIT_HASH = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def phone_chars(digits):

    return char_helper(digits, 0, "", [])


def char_helper(digits, level, current, subsets):
    # Our non-exit exit
    if len(current) == len(digits):
        subsets.append(current)
        return

    for i in DIGIT_HASH[digits[level]]:
        temp_current = current + i
        char_helper(digits, level+1, temp_current, subsets)

    return subsets



print(phone_chars("234"))
print(phone_chars("23"))
print(phone_chars("2"))
