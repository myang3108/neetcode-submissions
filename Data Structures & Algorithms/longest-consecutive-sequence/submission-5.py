class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums) # use a set to get rid of duplicates

        for i in numset:
           # want to first check if this is the start
           if i - 1 not in numset:
                length = 1
                while i + length in numset:
                    length += 1
                longest = max(longest, length)
           
        
        return longest
