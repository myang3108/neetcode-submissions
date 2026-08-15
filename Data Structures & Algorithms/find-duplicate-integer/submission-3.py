class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        # lets use cyclic sort!
        while i < len(nums):
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        ans = -1
        for n in range(len(nums)):
            if nums[n] != n+1:
                ans = nums[n]
        return ans        
