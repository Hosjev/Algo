def dups(nums, target):
    if len(nums) == 0: return 0

    position = classic_bs(0, len(nums) - 1, nums, target)
    answer = [position]

    if answer == -1: return [-1, -1]

    L = position - 1
    while L >= 0:
        try:
            if nums[L] == target:
                answer.append(L)
                L -= 1
            else: break
        except IndexError:
            break

    R = position + 1
    while R < len(nums):
        try:
            if nums[R] == target:
                answer.append(R)
                R += 1
            else: break
        except IndexError:
            break

    print(answer)
    answer.sort()
    return [answer[0], answer[-1]]


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


n = [1, 2, 2, 4, 5, 5, 5, 6, 7, 7, 7,7]
t = 7
n = [1]
t = 1
print(dups(n, t))
