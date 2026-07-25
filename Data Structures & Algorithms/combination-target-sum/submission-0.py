class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        currlist = []

        def backtrack(i, currsum):
            if currsum == target and currlist not in sol:
                sol.append(currlist[:])
            
            if i == len(nums) or currsum > target:
                return
        # base case -> either target too big, reach the end, or we get what we want

        # you can either never use the number again - dont pick scenario
            backtrack(i+1, currsum)

        # or use the number and then make it availble again - pick scenario
            currlist.append(nums[i])
            backtrack(i, currsum + nums[i])
            currlist.pop() # pop right

        backtrack(0,0)
        return sol



