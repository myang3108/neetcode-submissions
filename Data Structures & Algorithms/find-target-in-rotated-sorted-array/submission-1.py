class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # find pivot first # smallest idx
        # do it on the correct side
        
        s = 0
        e = len(nums) - 1
        pivot = -1 # smallest idx

        while s < e:
            m = (s + e) // 2
            if nums[m] > nums[e]:
                s = m + 1
            else:
                e = m
        
        pivot = s
        print(pivot)

        # look on either left or right half -> look on right half
        if target >= nums[pivot] and target <= nums[-1]:
            s = pivot
            e = len(nums) - 1
        else:
            s = 0
            e = pivot

        while s <= e:
            m = (s + e) // 2
            if nums[m] < target:
                s = m + 1
            elif nums[m] > target:
                e = m - 1
            elif nums[m] == target:
                return m

        return -1




        
        return -1