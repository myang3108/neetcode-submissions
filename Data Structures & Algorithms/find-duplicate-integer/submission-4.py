class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        # lets use cyclic sort!
        while i < len(nums):
            correct_index = nums[i] - 1  # where this value SHOULD live
            if nums[i] != nums[correct_index]: # if the guy isnt where he should be
                nums[i], nums[correct_index] = nums[correct_index], nums[i] # swap him
            # keep going until we get the guy into the right seat
            else:
                i += 1 # if he is then move on

        ans = -1
        for n in range(len(nums)):
            if nums[n] != n+1:
                ans = nums[n]
        return ans        
