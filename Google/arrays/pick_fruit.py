from typing import List



class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # EC
        if len(fruits) <= 2 or \
          len(set(fruits)) <= 2:
            return len(fruits)
        
        # Prime
        max_pick = int()
        L, R = 0, 1

        # Logic
        while R < len(fruits):
            if len(set(fruits[L:R+1])) <= 2:
                max_pick = max(max_pick, R-L+1)
                R += 1
            else:
                L += 1
        return max_pick    
            

if __name__ == "__main__":
    f = [3,3,3,1,2,1,1,2,3,3,4]
    obj = Solution()
    print(obj.totalFruit(f))
