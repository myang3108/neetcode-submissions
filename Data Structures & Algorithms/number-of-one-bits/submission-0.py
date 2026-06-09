class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(32):
            # do a mask at that specific place to see if its a 1 or 0 at that place
            # if the number isnt 0 then its set
            if ((1 << i) & n):
                res += 1
        
        return res