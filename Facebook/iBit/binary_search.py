def bs(arr, L, R, t):
    if L == R:
        if arr[L] == t:
            return L
        else: return -1
    M = (L+R) // 2
    if arr[M] == t:
        return M
    if t < arr[M]:
        R = M - 1
    else:
        L = M + 1

    return bs(arr, L, R, t)


n = [1, 2, 3, 5, 6, 7, 8]
t = 14
print(bs(n, 0, len(n)-1, t))
