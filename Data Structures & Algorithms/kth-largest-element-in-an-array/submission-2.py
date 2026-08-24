class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        # loop through the array and once the minheap gets to size k, pop from it
        # at the end the head will be the smallest
        # if we use a maxheap we'll have too push the entire array onto the heap
        
        for n in nums:
            heapq.heappush(heap, n)
            while len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]