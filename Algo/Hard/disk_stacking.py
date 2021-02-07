"""
Given a non-empty array of arrays where each triad represents a disk. The #'s represent: width, depth, height. Stack up the disks to maximize the height of the stack. A disk must have a strictly smaller width, depth and height than any below it.

Your function should return an array of the disks in the final stack, starting with the top disk and ending with the bottom disk. Note that you can't rotate disks; in other wods, the ints in each subarray must be [width, depth, height] at all times.

Input:
    disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]

Output:
    [[2, 1, 2], [3, 2, 3], [4, 4, 5]]

answer - O(N^2)T O(N)S
"""

def diskStacking(disks):
    """
    Arrange my disks by height since I'm looking for a max of height possible.
        [[1, 3, 1], [2, 1, 2], [3, 2, 3], [2, 3, 4], [4, 4, 5], [2, 2, 8]]
    Create an array of heights only.
        heights = [ 1, 2, 3, 4, 5, 8]
    Iterate thru my disks and compare from smallest to largest the sums of which can be added.
        heights = [ 1, 2, 5, 4, 10, 8]

    """
    disks.sort(key=lambda idx: idx[2])

    only_height = [ x[2] for x in disks ]

    for idx in range(1, len(disks)):
        for prev in range(idx): # 0 to myself
            # Skip entirely if our height is equal
            if disks[idx][2] == disks[prev][2]: continue
            # Width / Depth
            if (disks[prev][0] < disks[idx][0]) and (disks[prev][1] < disks[idx][1]):
                only_height[idx] = max(only_height[idx], disks[idx][2] + only_height[prev])

    #print(only_height)
    count = max(only_height)
    answer = []
    while count != 0:
        idx = only_height.index(count)
        answer.append(disks[idx])
        count = count - disks[idx][2]

    return sorted(answer, key=lambda idx: idx[2])


if __name__ == "__main__":

    disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]

    print(diskStacking(disks))
