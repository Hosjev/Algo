def matching_brackets(s: str) -> bool:
    """
    1. make empty stack (LIFO)
    2. make hash where key=Right side, val=L
    3. run through "s"
       a. if character NOT R, add to stack
       b. if char R, pop from stack
       c. if match to hash value, cont, else R False
    4. edge cases: a)empty stack, b)items left on stack
    """

    stack = []

    complete_sets = {
        "]": "[",
        ")": "(",
        "}": "{"
    }

    for character in s:
        if character not in complete_sets:
            stack.append(character)
        else:
            # Right Side
            try:
                left_side = stack.pop()
                if left_side != complete_sets[character]:
                    return False
            except IndexError:
                return False

    # A final return
    return False if stack else True


print(matching_brackets("{()[]}"))
print(matching_brackets("{()]}"))
