from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # EC
        # Prime
        from collections import defaultdict
        cache = defaultdict(list)
        for position in points:
            key = pow(position[0], 2) + pow(position[1], 2)
            cache[key].append(position)
            
        # Second part
        answer = []
        keys = sorted(cache.keys())
        for key in keys:
            for i in range(len(cache[key])):
                answer.append(cache[key][i])
                if len(answer) == k:
                    return answer
        # K could be larger, so a final return
        return answer[:k]


if __name__ == "__main__":
    p = [[1,3],[-2,2]]
    obj = Solution()
    print(obj.kClosest(p, 1))
