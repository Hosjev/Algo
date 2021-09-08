"""
A positive integer is considered uniform if all of its digits are equal. For example, 222222 is uniform, while 223223 is not.
Given two positive integers AA and BB, determine the number of uniform integers between AA and BB, inclusive.
"""
# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    # Write your code here
    # Somewhat base ten

    answer = [0]

    match = get_uniform(A, B, answer)
    decimal = convert_decimal(match)

    while not match > B:
        match = match + decimal
        # Our match skipped decimals
        if len(str(match)) != len(str(decimal)):
            match = get_uniform(match, B, answer)
            if not match: break
            decimal = convert_decimal(match)
        elif match == B:
            update_answer(answer)
            break
        elif match > B:
            break
        else:
            update_answer(answer)

    return answer[0]


def update_answer(answer):
    answer[0] = answer[0] + 1


def get_uniform(start: int, B: int, answer) -> int:
    match = False
    D = int()
    for D in range(start, B + 1):
        D = str(D)
        match = recur(D, D[0], D[0], len(D)-1)
        if match:
            update_answer(answer)
            break
    return int(D)


def recur(digits: str, current: str, match: str, idx: int):
    # Return boolean
    if current != match:
        return False
    elif idx < 0:
        return True
    return recur(digits, match, digits[idx-1], idx-1)



def convert_decimal(number: int) -> int:
    # Return 11, 111, 1111
    #adder = str()
    #for x in range(len(str(number))):
        #adder += "1"
    #return int(adder)
    return int("1" * number)



if __name__ == "__main__":
    # answer = 77-9=3; 111-9=9; 1111-2=2 ==14
    print(getUniformIntegerCountInInterval(76, 3000))
    print(getUniformIntegerCountInInterval(1, 9)) # 9
    #print(getUniformIntegerCountInInterval(999999999999, 999999999999)) # 1
