"""
WATCH SPACE-TIME COMPLEXITY.
Write function that takes non-empty array of distinct ints AND int that reps target sum.
Input:
    [ 3, 5, -4, 8, 11, 1, -1, 6]
    10
Output:
    [-1, 11]

If any 2 nums in the array sum up to target, return as list.
If not, return empty arra.
*Don't sum the int itself (clue to track processed nums).
*Guarantee of one answer

"""


def twoNumberSum(num_arr, target_sum):
    # iterate thru nums by index?
    # for first num add next, stop is target reached
    # O of N?
    n = len(num_arr)-1 #8

    while n != 0:
        for x in range(len(num_arr)): # O of N approaching log(N)
            if n == x: continue # O(1)
            if (num_arr[n] + num_arr[x]) == target_sum: # O(1)
                return [num_arr[n], num_arr[x]]
        n -= 1

    return []


def twoNumberSum(num_arr, target_sum):
    # Hash table version cuts down on TC
    answers = dict()
    for x in num_arr: # O(N)
        answers[x] = target_sum - x 

    # Iterate thru answers
    for k,v in answers.items():
        for x in range(len(num_arr)): # 0-7
            #print(f"...inside for, k-x: {k,num_arr[x]}")
            if k == num_arr[x]: continue # not quite right, should be "index number"
            if v == num_arr[x]: return [k, num_arr[x]]

    return []



if __name__ == "__main__":
    arr = [ 3, 5, -4, 8, 11, 1, -1, 6]
    ts = 10
    print(twoNumberSum(arr, ts))
