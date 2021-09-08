def occurrence_of(haystack, needle):
    """
    1. divide haystack into sets
       a. haystack - needle + 1 = number of sets
    2. linear iterate, return 1st occurrence
    3. edge cases
       a. return 0 if either empty
       b. return -1 finally
    O(N-needle) -- worst case; best case 1st return O(1)
    """
    if not needle: return 0

    n_sets = len(haystack) - len(needle) + 1

    # Do this thing, this many times
    for idx in range(n_sets):
        if haystack[idx:idx+len(needle)] == needle:
            return idx

    # A final return
    return -1


print(occurrence_of("hello", "ll"))
print(occurrence_of("aaaaaaaaaa", "bba"))
