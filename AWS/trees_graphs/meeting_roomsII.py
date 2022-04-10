class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Prime
        used_rooms = 0
        times_start = sorted(i[0] for i in intervals)
        times_end = sorted(i[1] for i in intervals)
        num_of_meets = len(intervals)
        startP = 0
        endP = 0

        # [[0,30],[5,10],[15,20]]
        # [[2,4], [7,10]]
        # ASSUME we need a room but take away if start time past last end time
        while startP < num_of_meets:
            if times_start[startP] >= times_end[endP]:
                used_rooms -= 1 # => room avail
                endP += 1
            used_rooms += 1    
            startP += 1   

        return used_rooms
