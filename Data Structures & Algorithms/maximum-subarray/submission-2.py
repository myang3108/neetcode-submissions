class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # for each element, either start
        # of new subarray or part of existing one

        # need a currsum and maxsum
        # if currsum < 0 -> prefix is not helping us -> set to 0

        currsum = 0
        maxsum = float('-inf')
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            currsum += nums[i]
            maxsum = max(currsum, maxsum)
            # do it after since we need to first get the maxsum
            if currsum < 0:
                currsum = 0

        return maxsum