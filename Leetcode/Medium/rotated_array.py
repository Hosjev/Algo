def search_rotate(nums, target):

    offset = pattern_bs(0, len(nums)-1, nums)
    if not offset:
        offset = 0
    nums.sort()
    position = classic_bs(0, len(nums) - 1, nums, target)

    return -1 if position == -1 else (position + offset) % len(nums)


def classic_bs(L, R, array, target):
    if L >= R:
        if array[L] == target:
            return L
        else:
            return -1
    middle = L + ((R-L) // 2)
    if array[middle] == target:
        return middle
    elif array[middle] > target:
        L, R = L, middle - 1
    else:
        L, R = middle + 1, R
    return classic_bs(L, R, array, target)


def pattern_bs(L, R, array):
    if L == R:
        return
    M = L + ((R - L) // 2)
    left_L, left_R = L, M
    right_L, right_R = M+1, R
    
    if array[left_R] > array[right_L]:
        return right_L

    left = pattern_bs(left_L, left_R, array) 
    if not left:
        return pattern_bs(right_L, right_R, array)
    else:
        return left


n = [5, 1, 3]
t = 1
print(search_rotate(n, t))
