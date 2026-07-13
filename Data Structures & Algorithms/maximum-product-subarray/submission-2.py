class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minnum = 1
        maxnum = 1
        res = nums[0]

        # if we use that number, it can either contribute to the min product
        # or max product
        # save both
        for n in range(len(nums)):
            print("old", maxnum, minnum)
            tmp = maxnum
            maxnum = max(tmp * nums[n], minnum * nums[n], nums[n])
            minnum = min(minnum * nums[n], tmp * nums[n], nums[n]) # either extend maxnum, minnum, or start fresh
            print("new", maxnum, minnum)
            res = max(maxnum, res)
            print(res)
        

        return res