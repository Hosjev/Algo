"""
Write function that takes non-empty array of distinct ints and an int representing the target sum.
The function should find all triplets in the array that sum up to the target and return a 2D array of 
the triplets. The nums in each triplet should be ordered in ascending order and the triplets 
themselves should be ordered with respect to the numbers they hold.
Input:
    array = [ 12, 3, 1, 2, -6, 5, -8, 6]
    targetSum = 0
Output:
    [ [-8, 2, 6], [-8, 3, 5], [-6, 1, 5] ]

* if no three nums add up, function returns an empty array
* sum pairs? then iterate thru remaining ints?
* forward then backward (skipping backward adjacent index)
* we could pass pairs to a recursive func that takes pairs and arr
    or it takes position1, 2 and third (third is what iterates thru loop
* Pairs not working. Obvi.
answer - O(N^2)T / O(N)S
"""

def threeNumberSum(arr, ts):
    # The Algo. This Whole thing is predicated on the sort.
    # As you're able to guarantee less/greater values left/right.
    arr.sort() # Cheating!!!
    answer = []
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            cs = arr[i] + arr[left] + arr[right]
            if cs == ts:
                answer.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif cs < ts:
                left += 1
            elif cs > ts:
                right -= 1
    return answer

def threeNumberSum(array, target_sum):

    def swap(posA, posB):
        return posB, posA

    def bubble_sort(ts, arr_len):
        # Rewrite below as bubble sort then rewrite function again
        finished = True
        for idx in range( arr_len ):
            if ts[idx] > ts[idx+1]:
                ts[idx], ts[idx+1] = swap(ts[idx], ts[idx+1])
                finished = False
        if finished: return ts
        else: return bubble_sort(ts, arr_len-1)


    answer = []
    # Iterative version based on sorted first
    bubble_sort(array, len(array)-1)
    for idx in range(len(array)-2):
        L = idx+1
        R = len(array)-1
        while L < R: # Favoring left due to for loop
            cs = [array[idx], array[L], array[R]]
            ts = sum(cs)
            if ts == target_sum:
                answer.append(cs)
                L += 1
                R -= 1
            elif ts < target_sum: L += 1 # increase sum
            elif ts > target_sum: R -= 1 # decrease sum

    return answer

    # Iterative version based on non-sorted
    def loops(array, answer):
        for x in range(len(array)):
            for y in range(x+1, len(array)):
                for z in range(y+1, len(array)):
                    ts = [array[x], array[y], array[z]]
                    if sum(ts) == target_sum:
                        answer.append(bubble_sort(ts, len(ts)-1))
        return sorted(answer)

    #return loops(array, answer)

    def make_array(p1, p2, backward):
        if backward:
            return [i for i in range(p1-2, -1, -1)]
        else:
            # On the end length, we go ONE more to trip backward
            return [i for i in range(p2+1, len(array)+1, 1)]


    def inner_sum(p1, p2, arr):
        # Pairing dumb idea
        if p1 < 0: return
        if p2 == len(array): return
        for x in arr:
            if x == len(array):
                return inner_sum( p1, p2, make_array(p1, p2, True))
            ts = [array[p1], array[p2], array[x]]
            if sum(ts) == target_sum:
                answer.append(sort(ts))

        return inner_sum(p1+1, p2+1, make_array(p1, p2, False))



if __name__ == "__main__":
    array = [ 12, 3, 1, 2, -6, 5, -8, 6]
    array = [12, 3, 1, 2, -6, 5, 0, -8, -1]
    # ans [[-8, 3, 5], [-6, 1, 5], [-1, 0, 1]]
    target_sum = 0

    print(threeNumberSum(array, target_sum))
