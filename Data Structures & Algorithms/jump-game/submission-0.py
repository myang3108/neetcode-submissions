class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal = n - 1
        # start iterating from n-2
        # if n-2 + nums[n-1] >= n-1
        # then n-2 becomes the 'new start'
        # how do we go backwards from there?
        # we set it to da new goal!!!!!!

        goal = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        
        if goal == 0:
            return True
        else:
            return False