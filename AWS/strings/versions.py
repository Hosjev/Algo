from typing import List



class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n1, n2 = len(v1), len(v2)

        # compare versions
        for i in range(max(n1, n2)):
            i1 = int(v1[i]) if i < n1 else 0
            i2 = int(v2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1

        # the versions are equal
        return 0


if __name__ == "__main__":
    obj = Solution()
    print(obj.compareVersion("1.0.1", "1.0"))
