class Solution:
    def sortColors(self, A):
        # Bucket sort O(N + 2) array-buckets [0, 1, 2]
        #    -iterate thru 1st, fill buckets
        #    -iterate thru and fill array based on buckets
        buckets = [0, 0, 0]
        for i in A:
            if i == 0:
                buckets[0] += 1
            elif i == 1:
                buckets[1] += 1
            elif i == 2:
                buckets[2] += 1

        start = 0
        for idx, bucket in enumerate(buckets):
            if bucket > 0:
                A[start:start + bucket] = [idx] * bucket
                start = start + bucket

        return A

A = [2,1,0,0,2,1,1,1,1,2,0,0,1]
A = [0]
print(Solution().sort(A))
