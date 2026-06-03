"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if intervals == []:
            return 0
        intervals.sort(key=lambda x: x.start)
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0].end)
        
        # lets use a minheap instead - keep track of end times
        # if we have a later end time then we can push onto the heap
        # if earlier end time we push new one onto the heap to signify a new room
        # draw dat shi out
        # at the end we check how big the heap is

        for i in range(1, len(intervals)):
            if intervals[i].start >= free_rooms[0]:
                # Remove that room's old end time from the heap
                heapq.heappop(free_rooms)
                
            # Add the current meeting's end time to the heap
            # (Either updating the room we just popped, or opening a new room)
            heapq.heappush(free_rooms, intervals[i].end)

        print(free_rooms)
        return len(free_rooms)