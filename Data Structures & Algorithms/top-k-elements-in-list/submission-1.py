class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # put the count into a hashmap
        mp = defaultdict(int)
        for n in nums:
            mp[n] += 1
        # put the tuple (value, key) into a maxheap
        # then pop the top k largest ones from the top and return them in a list
        res = []
        pq = [] # heap is a list

        for num, freq in mp.items():
            pq.append((freq, num))

        heapq.heapify_max(pq)
        
        while k > 0:
            currFreq, currNum = heapq.heappop_max(pq)
            res.append(currNum)
            k -= 1

        return res