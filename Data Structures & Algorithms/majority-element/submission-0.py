class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        for n in nums:
            mp[n] += 1
            if mp[n] > len(nums) // 2:
                return n
        