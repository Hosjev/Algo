"""
Write a function that takes in an array of ints in a 2D matrix. Return the ints by way of zigzag--meaning Down, up, across, down, down, up, down or across, down, etc.

Input:
    array = [
        [1,  3,  4, 10],
        [2,  5,  9, 11],
        [6,  8, 12, 15],
        [7, 13, 14, 16]
    ]

Output:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

answer - O(N)T / O(N)S
"""

# I wrote this whole fucking thing after reading "that can be squared shaped"
def zigzagTraverse(array):
    ordered = []

    # The forward pass to middle
    for bit in range(len(array)):
        if (bit % 2) == 0: # 0 would be even
            row, col, ion = 0, bit, "pos"
        else: # odd
            row, col, ion = bit, 0, "neg"
        recur_zigzag(array, ordered, bit, ion, row, col, 0)

    # The reverse, directions change
    for bit in reversed(range(1, len(array))):
        if (bit % 2) == 0: # 0 would be even
            row, col, ion = len(array)-1, len(array)-bit, "neg"
        else: # odd
            row, col, ion = len(array)-bit, len(array)-1, "pos"
        recur_zigzag(array, ordered, bit, ion, row, col, 1)

    return ordered


def recur_zigzag(array, ordered, bit, ion, row, col, count):
    if count > bit:
        return ordered

    ordered.append(array[row][col])

    if ion == "pos": # Even
        row += 1
        col -= 1
    else: # Odd
        row -= 1
        col += 1
    return recur_zigzag(array, ordered, bit, ion, row, col, count+1)


def zigzagTraverse(array):
    # The version that actually traversed the boundaries
    ordered = []
    row, col = 0, 0
    height = len(array)-1
    width = len(array[0])-1
    go_Down = True

    print(height,width)
    while not out_of_bounds(width, height, row, col):
        ordered.append(array[row][col])
        if go_Down: # go_Down set
            if (col == 0) or (row == height): # edge moves
                go_Down = False
                # These 2 next conditions MUST be in this order
                if row == height: col += 1
                if col == 0: row += 1
            else: # normal middle move
                row += 1
                col -= 1
        else: # go_Up set
            if row == 0 or col == width: # edge moves
                go_Down = True
                # These 2 next conditions MUST be in this order
                if col == width: row += 1
                if row == 0: col += 1
            else: # normal middle move
                row -= 1
                col += 1

    return ordered

def out_of_bounds(width, height, row, col):
    return row < 0 or col < 0 or row > height or col > width


if __name__ == "__main__":

    array = [
        [1,  3,  4, 10],
        [2,  5,  9, 11],
        [6,  8, 12, 15],
        [7, 13, 14, 16]
    ]

    print(zigzagTraverse(array))
