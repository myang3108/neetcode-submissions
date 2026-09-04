class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # need prefix sum
        # we have a prefix map that stores the running total
        # if we want to find a middle subarray see if big total - some prefix map total = k
        # so we check big total - k for the prefix map index
        mp = defaultdict(int)
        mp[0] = 1
        total = 0
        res = 0
        for n in nums:
            total += n
            if total - k in mp:
                res += mp[total - k]
            
            mp[total] += 1
        
        return res

