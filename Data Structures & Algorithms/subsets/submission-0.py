class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # track the index
        # either choose it or dont choose it
        # once we choose it we cant go back -> move the idx forward
        # backtrack once we exausted all options for that one

        # edge cases - reach the end of the index and we've exausted all possible options
        # dont pick it
        # add the current number and then dont forget to undo it

        res = []
        curr = []

        def backtracking(i):
            if i >= len(nums): # reached the end of the line so we add in the current array
                res.append(curr.copy())
                return
            
            # dont use i -> skip
            backtracking(i+1)

            # use i -> append to curr and then move i
            curr.append(nums[i])
            backtracking(i+1)
            curr.remove(nums[i])
        
        backtracking(0)
        return res