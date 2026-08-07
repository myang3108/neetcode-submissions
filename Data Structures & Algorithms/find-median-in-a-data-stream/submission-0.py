class MedianFinder:

    # need to have 2 priority queues: one minheap for the right side, one maxheap for hte left side


    # maxheap _head_ | _head_ minheap

    # have the left side have up to 1 more than the right side
    # even -> pop from each and average
    # odd -> pop from left side

    def __init__(self):
        self.leftside = []
        self.rightside = []
        
    def addNum(self, num: int) -> None:
        # first add it to the left side
        heapq.heappush_max(self.leftside, num)
        # then put something from the left to the right side
        # if the right side is too big put it back on the left to balance it out
        largest_left = heapq.heappop_max(self.leftside)
        heapq.heappush(self.rightside, largest_left)

        if len(self.rightside) > len(self.leftside):
            smallest_right = heapq.heappop(self.rightside)
            heapq.heappush_max(self.leftside, smallest_right)
        

    def findMedian(self) -> float:
        if (len(self.rightside) + len(self.leftside)) % 2 != 0:
            return self.leftside[0]
        else:
            return (self.leftside[0] + self.rightside[0]) / 2.0
        
        