def container(height):

    # breaks runtime
    if len(height) <= 1: return 0

    # Init/prime
    max_volume = 0
    left = 0
    right = len(height) - 1

    while left < right:
        running_max = min(height[left], height[right]) * (right - left)
        max_volume = max(max_volume, running_max)
        # Alternate L and R favoring max heights
        if height[left] < height[right]:
           left += 1
        else:
           right -= 1

    return max_volume


h = [1, 8, 3, 4, 6, 5, 2, 4, 7]
#h = [1, 8, 3]
#h = [1, 2, 1]
#h = [1, 2, 4, 3] # 4
h = [2,3,10,5,7,8,9] # 36

print(container(h))
