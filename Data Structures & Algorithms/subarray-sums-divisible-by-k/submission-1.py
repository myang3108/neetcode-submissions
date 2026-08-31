class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # use a prefix sum
        # we know that if two things have the same remainder when we mod, when we subtract from each other they will be divisible by k

        count = defaultdict(int) # remainder = k, count = value
        count[0] = 1 # imagine we have [5] -> remainder 0 -> we need something to compare to it
        res = 0
        prefix = 0
        for n in nums:
            prefix += n
            remainder = prefix % k
            if remainder in count:
                res += count[remainder]
                
            count[remainder] += 1

        return res