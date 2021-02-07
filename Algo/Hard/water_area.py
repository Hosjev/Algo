"""
You're given an array of non-negative ints where each non-zero int represents the height of a pillar of width = 1. Imagine water being poured over all of the pillars. And write a function that returns the surace area of the water trapped between the pillars viewed from the front. Note that spilled water should be ignored.

Input:
    heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]

Output:
    48

* clarity - this means, starting at index 0, each number moves ONCE
            and each INDEX is visited ONCE and finally returns to 0
* if new position never passes starting point 0
  if number of moves is never greater than length of array, fail?
answer - O(N)T O(1)S
"""

def waterArea(array):
    """
    In my version, I do this:
        create hash of every point in between defined edges, 8 and 3 above
        use indices as keys
        in a while loop, with first pillar as HighPoint var, advance to pools
        if pool, add HP # to hash, continue
        if pillar, if Greater than, do nothing but reset HP
        if pillar, if less than, set LP to array[pillar]
        On reverse, if pillar
            add HP minus array[pillar] to hash
            we run this all the way to HP index, subtracting HP-LP out of hash pools
        Finally, sum the values in hash
        You could even ADD pillars as water volume in hash keys with a value then subtract at end
        * subtract middle pillar heights
        * I would somehow need to Know or mark middle pillars and edge pillars
        * This doesn't necessarily need to be a whole O(N) operation, we could identify them as we go

    Better written sol:
        Same hash table with everything entry/key btw edges
        Iterate straight thru
        HP = 1st
        * if pool, add value of HP to hash
        * elif pillar(a non-zero) and < HP, backtrack to HP and subtract HP-pillar
        * elif pillar(a non-zero) and > HP, backtrack to HP and add diff of current HP to all pools/pillars entries; Finally, set a new HP
        * elif same, do nothing
        * until we reach last pillar (edge)
        * return sum of hash values

    *Algo sol 1:
        store left max for each point in heights
        store right max
        store new array with diff btw current value and max/min

    """

    left = [0]
    max_left = 0
    for x in range(1, len(array)):
        max_left = max(max_left, array[x-1])
        left.append(max_left)

    right = [0]
    max_right = 0
    for x in reversed(range(len(array)-1)):
        max_right = max(max_right, array[x+1])
        right.insert(0, max_right)

    pools = [None] * len(array)

    for idx in range(len(array)):
        min_height = min(left[idx], right[idx])
        if array[idx] < min_height:
            pools[idx] = min_height - array[idx]
        else:
            pools[idx] = 0

    return sum(pools)



if __name__ == "__main__":

    heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]

    print(waterArea(heights))
