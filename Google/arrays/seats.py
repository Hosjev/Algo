from typing import List



class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # Prime
        left, right = [0] * len(seats), [0] * len(seats)
        for i in range(len(seats)): # leftmost
            if seats[i] == 1:
                left[i] = None
            else:
                if i == 0: # our index is 0 AND we are empty
                    left[i] = float("inf")
                else: # not 0
                    if left[i-1] is not None: left[i] = left[i-1]
                    else: left[i] = i-1
        for i in range(len(seats)-1, -1, -1): # rightmost
            if seats[i] == 1:
                right[i] = None
            else:
                if i == len(seats)-1: # our index is last
                    right[i] = float("inf")
                else:
                    if right[i+1] is not None: right[i] = right[i+1]
                    else: right[i] = i+1

        # 2nd Prime
        base_min = 0

        # Logic
        for idx in range(len(seats)):
            if left[idx] is not None: # only eval avail seats
                if left[idx] != float("inf"): left[idx] = abs(left[idx] - idx)
                if right[idx] != float("inf"): right[idx] = abs(right[idx] - idx)
                local_min = min(left[idx], right[idx])
                if local_min > base_min:
                    base_min = local_min
        return base_min


if __name__ == "__main__":
    s = [1, 0,0,0,1,0,1]
    print(Solution().maxDistToClosest(s))
