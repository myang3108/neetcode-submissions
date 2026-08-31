class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if right > middle -> the pivot is on the 
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # we need to find the pivot first and then do it a search on the correct side
             # pivot must be somewhere to the right
            if nums[m] > nums[r]:
                l = m + 1
            # pivot could be m or somewhere to the left
            else:
                r = m
        
        pivot = l # this is the smallest item in the array -> where the cutoff starts

        def binary(l, r, target):
            # does a binary search and returns the index if its found or -1 if its not found

            while l <= r:
                m = (r+l) // 2
                if nums[m] == target:
                    return m
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
            
            return -1
        
        res = binary(0, pivot, target) # does the pivot
        if res != -1:
            return res
        if res == -1:
           return binary(pivot, len(nums)-1, target)
            


