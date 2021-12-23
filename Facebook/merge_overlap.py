class Solution:
    
    def merge(self, intervals):
        # Return nested Lists
        if len(intervals) <= 1: return intervals

        # Prime
        intervals.sort(key=lambda x: x[0])
        overlapped = [intervals[0]]
        for i in range(1, len(intervals)):
            over_len = len(overlapped)
            left = intervals[i][0]
            right = intervals[i][1]
            last_left = overlapped[over_len - 1][0]
            last_right = overlapped[over_len - 1][1]
            if last_right >= left:
                overlapped[over_len - 1][0] = min(last_left, left)
                overlapped[over_len - 1][1] = max(last_right, right)
            else:
                overlapped.append(intervals[i])

        return overlapped


if __name__ == "__main__":
    i = [ [1,5], [4,6], [2,3], [8,12], [1,3], [11,15] ]
    print(Solution().merge(i))
