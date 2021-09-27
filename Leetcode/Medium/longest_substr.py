def longest_substring(s):
    """
    1. create an object to hold max
    2. create a hash table to hold unique characters
       and add their index position as we go
       "char": "014" etc.
    3. create an object to hold a running substring
    4. update the max object at the end of every run
       return max obj
    ** linear read through string, O(N) best time
    """
    running_substring = ""
    answer = int()
    char_hash = {}

    for idx in range(len(s)):
        if s[idx] not in running_substring:
            running_substring += str(s[idx])
        else:
            # Our character is somewhere
            running_substring = s[char_hash[s[idx]] + 1:idx + 1] 

        # Next to last
        answer = max(answer, len(running_substring))

        # Last thing we do, just an update for last known
        char_hash[s[idx]] = idx

    return answer



s = "babcababb"
s = "alqebriavxoo" # me - 11; them - 10
#     lqebriavxo

print(longest_substring(s))
