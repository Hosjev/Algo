def roman_convert(num):
    """
    Convert integer to string of roman numeral
    ** conditions -- each prior can be subtracted to make fraction
       4 = IV
       9 = IX
       1994 = MCMXCIV
    ** constraints 1 <= num <= 3999
    """
    roman_hash = {
         1000: "M", # M
         500: "D",  # D
         100: "C",  # C
         50: "L",   # L
         10: "X",   # X
         5: "V",    # V
         1: "I"     # I
    }

    # Result
    answer = ""

    for idx, integer in enumerate(reversed(str(num))):
        # Wretched but...
        multiplier = int("1" + ("0" * idx))
        integer = int(integer)
        if integer == 1:
            answer = (roman_hash[1*multiplier] * (1)) + answer
        elif integer in [2, 3]:
            answer = (roman_hash[multiplier] * (integer)) + answer
        elif integer == 5:
            answer = (roman_hash[5*multiplier] * (1)) + answer
        elif integer == 4:
            answer = (roman_hash[multiplier] * (1)) + \
                     (roman_hash[5*multiplier] * (1)) + answer
        elif integer in [6, 7, 8]:
            answer = (roman_hash[5*multiplier] * (1)) + \
                     (roman_hash[multiplier] * (integer-5)) + answer
        elif integer == 9:
            answer = (roman_hash[multiplier] * (1)) + \
                     (roman_hash[10*multiplier] * (1)) + answer

    return answer

# 4 = 1, 5; 9 = 1, 10
# MCMXCIV
print(roman_convert(1994))
print(roman_convert(4))
print(roman_convert(9))
print(roman_convert(58))
print(roman_convert(8))
print(roman_convert(3))
