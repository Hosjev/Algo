# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        L, R = 0, n
        while not L >= (R - 1):
            P = (L + R) // 2
            if isBadVersion(P):
                R = P
            else:
                L = P
        return L if isBadVersion(L) == "bad" else R
        
        

def isBadVersion(version):
    # Mock the API return randomly
    return True if version in [i for i in range(3,11)] else False



if __name__ == "__main__":
    # The idea here is to run O(logN) given
    #   ALL versions of our software are bad >=
    #   any given version. We return the earliest.
    # Running this like a binary search, eliminate halves.
    n = [1,2,3,4,5,6,7,8,9,10]
    print(Solution().firstBadVersion(10))
