"""
 1      2       3
       abc     def
 4      5       6
ghi    jkl     mno
 7      8       9
pqrs   tuv     wxyz
        0

(Phone) Almost every digit is associated w/some letters in the alphabet. This allows certain phone #s to spell out actual words. For ex, the number 8464747328 is written timisgreat; or 2686463 is antoine or ant6463.

Note that a number doesn't represent a single sequence of letters, but rahter mulitple combos of letters. For ex, the digit 2 can repr 3 different letters (a, b, c).

A mnemonic is defined as a pattern of letters, ideas, or associations that assist in remembering something. Companies often use a mnemonic for their phone # to make it easier to remember.

Given a stringified # of any non-zero length, write a function that returns all mnemonics for this number. In any order.

For this problem, a valid mnemonic may only contain letters and the digits 0 and 1. In other words, if a digit is able to be repr'd by a ltter, then it must be. Digits 0 and 1 are the only 2 digits that don't have letter representations on the keypad (phone).

Note that you should rely on the keypad illustrated above for digit-letter assocs.

Input:
    phoneNumber = "1905"

Output:
    [
        "1w0j",
        "1w0k",
        "1w0l",
        "1x0j",
        "1x0k",
        "1x0l",
        "1y0j",
        "1y0k",
        "1y0l",
        "1z0j",
        "1a0k",
        "1z0l",
    ]

** this is the powerset and permutations problem
** on the above:
    (1) + (w,x,y,z) + (0) + (j,k,l)
** O()T | O()S
"""
import time


def phoneNumberMnemonics(phoneNumber):
    # Code
    list_of_subsets = getMnemonicSubs(phoneNumber)
    mnemonic_sets = []
    permutations_loop(list_of_subsets, mnemonic_sets, current_m="", idx=0)
    return mnemonic_sets


def permutations_loop(list_of_subsets, mnemonic_sets, current_m, idx):
    if idx == len(list_of_subsets):
        mnemonic_sets.append(current_m)
    else:
        # Item here is a set of strings
        for item in range(len(list_of_subsets[idx])):
            temp_current = current_m + list_of_subsets[idx][item]
            permutations_loop(list_of_subsets, mnemonic_sets,
                              temp_current, idx+1)


def getMnemonicSubs(phoneNumber):
    # Define the substitues
    # Ignore any digit checking for now
    # This should really be a global dict (DATA)
    digits = {
        "1": ["1"],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
        "0": ["0"]
    }

    subsets = []
    for digit in phoneNumber:
        subsets.append(digits[digit])

    return subsets


if __name__ == "__main__":

    phoneNumber = "1905"

    print(phoneNumberMnemonics(phoneNumber))
