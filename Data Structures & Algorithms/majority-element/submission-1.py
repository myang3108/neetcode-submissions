class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer moore
        # keep track of what the max num is with a single variable
        res = 0
        count = 0
        # if we see a number thats not current res -> decrement

        for n in nums:
            if count == 0:
                res = n # set n as the majority element

            if n == res:
                count += 1
            else:
                count -= 1
        
        return res


        