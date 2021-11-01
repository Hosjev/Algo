def find_nth(n, d):
    # Edge Case(s)
    if n > len(d):
        return -1
    count = 1
    cur = float("-inf")
    for k, v in sorted(d.items(), key = lambda x: x[1]):
        if count == n:
            return k
        if v > cur:
            count += 1
            cur = v
    return -1

