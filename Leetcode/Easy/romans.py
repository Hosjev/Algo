def convert_roman_to_integer(s: str) -> int:
    # 1. build hash table with keys as order
    #    and values as integers
    # 2. run through linear string and IF
    #    current key is greater than last key,
    #    add to answer last key value * 2
    # 3. store answer in array or just int
    # note--how bout we just say if current less than last?
    # O(N) -- best case in time b/c we must read input
    roman_hash = {
        "M": 1000, # M
        "D": 500,  # D
        "C": 100,  # C
        "L": 50,   # L
        "X": 10,   # X
        "V": 5,    # V
        "I": 1     # I
    }

    last_int = roman_hash["M"]
    answer_sum = 0
    for roman_numeral in s:
        current_int = roman_hash[roman_numeral]
        answer_sum += current_int
        # if current value is greater than last
        if current_int > last_int:
            answer_sum -= (last_int * 2)
        last_int = current_int

    return answer_sum


print(convert_roman_to_integer("MCMXV")) # 1915
print(convert_roman_to_integer("MCXV")) # 1115
