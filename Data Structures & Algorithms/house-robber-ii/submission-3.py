class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(smallerNums):
            # at each spot in the array ur either robbing the house or ur not -> 2 back + curr value or keep prev value
            if len(smallerNums) == 0:
                return 0
            if len(smallerNums) == 1:
                return smallerNums[0]
            
            twoaway = smallerNums[0]
            oneaway = max(smallerNums[1], twoaway)
            counter = 2
            
            
            while counter < len(smallerNums):
                curr = max(twoaway + smallerNums[counter], oneaway)
                twoaway = oneaway
                oneaway = curr
                counter += 1
            
            return oneaway
    
        if len(nums) == 1:
            return nums[0]
        ans1 = helper(nums[1:])
        ans2 = helper(nums[:-1])
        return max(ans1, ans2)

        
