class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for i in range(len(nums)):
            curr = 0
            while nums[i] + curr in nums:
                curr += 1
                longest = max(longest, curr)
        
        return longest
