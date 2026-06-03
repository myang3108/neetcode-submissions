class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        temp1 = 1
        temp2 = 2
        curr = 0

        for num in range(3, n+1):
            curr = temp1 + temp2
            print((num,curr))
            temp1 = temp2
            temp2 = curr
        
        return curr
