class Solution:
    def reverseBits(self, n: int) -> int:
        # if we have a 1 at the 1's place, left shift by 31 and then logic or
        # to set the msb place to 1

        res = 0 #32 0's

        for i in range(32):
            # first thing is get i'th bit of n:
            bit = 1 & (n >> i) #get the bit in the i'th spot
            res = res | (bit << (31-i))
        
        return res

