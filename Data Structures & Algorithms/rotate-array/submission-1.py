class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # easy way would be to put it in another array and then copy it back
        
        # reverse the input array
        # reverse back the first k elemeents -> reverse it back
        # reverse the remaining elements
        # this is single space

        # 5 4 3 2 1, k = 2
        # reverse 4 5 so then its 45321
        # reverse 321 (len - k elements) -> 45 123

        k = k % (len(nums))
        l = 0
        r = len(nums) - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l = 0
        r = k-1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l = k
        r = len(nums) - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
