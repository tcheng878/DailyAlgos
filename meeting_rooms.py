class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if len(intervals) == 0:
            return True
        times = []
        intervals.sort(key = lambda x: x[0])
        heapq.heappush(times, intervals[0][1])
        
        for i in intervals[1:]:
            if times[0] <= i[0]:
                heapq.heappop(times)
                
            heapq.heappush(times, i[1])
            
        print(times)
        if len(times) == 1:
            return True
        else:
            return False
            
            