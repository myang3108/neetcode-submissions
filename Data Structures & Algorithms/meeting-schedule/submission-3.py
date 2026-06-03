"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if intervals == []:
            return True
        merged = []
        intervals.sort(key=lambda x: x.start)
        merged.append(intervals[0])
        for i in range(1, len(intervals)):
            print((merged[-1].start, merged[-1].end))
            print((intervals[i].start, intervals[i].end))
            if intervals[i].start >= merged[-1].end:
                merged.append(intervals[i])
            else:
                return False
        
        return True
