"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # maximum number of overlaps at one time
        # aka minimum number of rooms we need to allocate
        # draw it out on pencil and paper for the timeline
        #the heap stores the end times of meetings currently occupying rooms the smallest end time is always at the top, representing the room that frees up the earliet
        # if a meeting starts after or at the same time another meeting ends, they can share the same room otherwise, we need a new room
        heap = []
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: x.start)
        heapq.heappush(heap, intervals[0].end)
        heapq.heapify(heap)

        for i in range(1, len(intervals)):
            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, intervals[i].end)
           

        return len(heap)





        