"""
Write function that takes 2 non-empty arrays of ints, finds the pair of numbers (one from each)
whose absolute difference is closest to zero, and returns an array with 1st num in position 0.
You can assume only one pair of numbers with the smallest difference.
Input:
    array_one = [-1, 5, 10, 20, 28, 3]
    array_two = [26, 134, 135, 15, 17]
Output:
    [28, 26]

* solution 1: iterate over array one, picking out single element and minus'ing
              keeping track of number and min amount
* solution 2: recursively feed array one to function, calling elements in two
              same minus'ing process
* both solutions more or less have the same TS complexity
* could we improve anything by sorting the numbers?
answer - O(N+M)T / O(N+M)S
"""
import time

def smallestDifference(aOne, aTwo):
    aOne.sort()
    aTwo.sort()
    idx_one = 0
    idx_two = 0
    smallest = float("inf")
    current = float("inf")
    pair = []
    while idx_one < len(aOne) and idx_two < len(aTwo):
        first = aOne[idx_one]
        second = aTwo[idx_two]
        if first < second:
            print(f"...condition first less second: {first, second}")
            current = second - first
            idx_one += 1
        elif second < first:
            print(f"...condition second less first: {second, first}")
            current = first - second
            idx_two += 1
        else:
            return [first, second]
        if smallest > current:
            smallest = current
            pair = [first, second]

    return pair


def SmallestDifference(arr1, arr2):

    def iter_diff(arr1, arr2):
        # My pair of indices and min variable
        pair = ( (None, None), float("inf") )
        for idx in range(len(arr1)):
            for idx2 in range(len(arr2)):
                diff = abs(arr1[idx] - arr2[idx2])
                if diff < pair[1]:
                    pair = ( (arr1[idx], arr2[idx2]), diff )
        return list(pair[0])

    return iter_diff(arr1, arr2)

def SmallestDifference(arr1, arr2):
    # The most time efficient but the messiest code
    arr1.sort()
    arr2.sort()
    answer = []
    answer.append(( (None, None), float("inf") ))
    idx_t = 0
    idx_b = 0
    u_quit = b_quit = False

    while not (u_quit and b_quit):
        time.sleep(.3)
        print(f"T B: {idx_t, idx_b}")
        top = arr1[idx_t]
        bottom = (arr2[idx_b], arr2[idx_b+1])

        left_sum = abs(abs(top) - abs(bottom[0]))
        right_sum = abs(abs(top) - abs(bottom[1]))

        print(f"...about to eval from current ans: {answer}")
        print(f"...Top, Bot, Ls, Rs: {top, bottom, left_sum, right_sum}")
        if left_sum <= right_sum:
            if answer[0][1] > left_sum:
                answer[0] = ( (top, bottom[0]), left_sum)
            # advance the left only if available
            if idx_t == len(arr1)-1:
                u_quit = True
                idx_b += 1
            else:
                idx_t += 1
        else:
            if answer[0][1] > right_sum:
                answer[0] = ( (top, bottom[1]), right_sum)
            # advance the right only if available
            if idx_b == len(arr2)-3:
                idx_b += 1
            elif idx_b == len(arr2)-2:
                b_quit = True
                if not u_quit: idx_t += 1
            else:
                idx_b += 2

    return list(answer[0][0])




if __name__ == "__main__":
    array_one = [-1, 5, 10, 20, 28, 3]
    array_two = [26, 134, 135, 15, 17]
    #array_one = [-1, 5, 10, 20, 3]
    #array_two = [26, 134, 135, 15, 17]
    array_one = [10, 0, 20, 25, 2000, 2001]
    array_two = [1005, 1006, 1014, 1032, 1031]
    array_one = [240, 124, 86, 111, 2, 84, 954, 27, 89]
    array_two = [1, 3, 954, 19, 8]


    print(smallestDifference(array_one, array_two))
