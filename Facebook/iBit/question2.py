def balance_ints(array):
    # Edge Case(s)
    if not len(array): return -1

    # Prime
    array.sort()
    max_count = 0
    count = 1
    balance_numbers = {}

    # 1st iteration
    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1

    # 2nd iteration
    count = 1
    array.append(float("inf")) # artifice to look back
    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            count += 1
        else:
            if not max_count == count:
                balance_numbers[array[i - 1]] = max_count - count
            count = 1

    return balance_numbers


A = [1, 2, 1, 1, 2, 3, 5]
print(balance_ints(A))
