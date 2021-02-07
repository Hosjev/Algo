"""
Write a function that takes in a string made up of brackets ( (, [, {, ), ], ] ) and other optional characters. The function should return a boolean representing whether the string is balanced with regard to the brackets.

A string is said to be balanced if it has as many opening brackets of a certain type as it has closing brackets of a certain type and if no bracket is unmatched. Note that an opening bracket can't match a corresponding closing bracket if it comes before it, and likewise, a closing bracket can't match a corresponding opening bracket that comes after it. Also, brackets can't overlap each other as in [(]).

Input:
    "({})(){}(())()()"

Output:
    True

* 1st version below has lots of constant time checks and works but the code could be cleaner by using the same logic but using a stack. So put left onto the stack until a right. Then pop (LIFO) and compare. If not match, fail. Also, ignore NOT L or R. 

O(n)T | O(n)S
"""
import time

def balancedBrackets(string):
    # Stack is for lefts
    stack = []

    approved_matches = {
        "{": "}",
        "[": "]",
        "(": ")"
        }
    lefts = approved_matches.keys()
    rights = approved_matches.values()

    if string[0] in lefts:
        for side in string:
            if side in lefts:
                stack.append(side)
            elif side in rights:
                left = stack.pop()
                # If my right equals the match in dict
                if side == approved_matches.get(left):
                    continue
                else:
                    return False
            else:
                pass
    else: return False

    return len(stack) == 0


def balancedBracketsW(string):
    # Make copy of string
    # 1. iterate
    # 2. is 0 Left? else False
    # 3. keep going till Right
    # This could work in a while loop as pairs
    # Like moving a pointer across the string and keeping track of index
    # if right == left in style and direction, pop the pair off, pointer
    #  should be in the right place and we keep working
    approved_matches = {
        "}": "{",
        "]": "[",
        ")": "("
        }

    if string[0] in approved_matches.values():
        rights = approved_matches.keys()
        lefts = approved_matches.values()
        copy_of_string = [i for i in string]
        pointer = 1

        # ([{]}) pointer lands at 3]
        while copy_of_string:
            # Our pointer didn't get a match and landed outside the array
            if pointer > len(copy_of_string)-1:
                return False
            # The pointer position isn't a closing bracket
            elif copy_of_string[pointer] not in rights:
                pointer += 1
            else:
                opening_side = approved_matches.get(copy_of_string[pointer])
                left = copy_of_string[pointer-1]
                if left == opening_side:
                    copy_of_string.pop(pointer)
                    copy_of_string.pop(pointer-1)
                    pointer -= 1
                elif left not in lefts and left not in rights:
                    copy_of_string.pop(pointer-1) # Trash it ([a]) ([])
                    pointer -= 1
                else:
                    return False
        return True

    else:
        return False

def balancedBracketsA(string):
    approved_matches = {
        "}": "{",
        "]": "[",
        ")": "("
        }

    lefts = approved_matches.values()
    rights = approved_matches.keys()
    stack = []

    # ( [ { } ] )
    for character in string:
        if character in lefts:
            stack.append(character)
        elif character in rights:
            if len(stack) == 0:
                return False
            if stack[-1] == approved_matches.get(character):
                stack.pop()
            else:
                return False
    return len(stack) == 0



if __name__ == "__main__":

    string = "([{}])" # T
    #string = "([{a}])" # T
    #string = "([{]})" # F
    #string = "()[]{}{" # F
    #string = "[((([])([]){}){}){}([])[]((())" # F
    #string = "][{]})" # F

    print(balancedBrackets(string))
