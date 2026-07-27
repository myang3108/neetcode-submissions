class Solution:
    def getSum(self, a: int, b: int) -> int:
        # first xor it -> doesnt take care of the carries
        # then add it to the anded version shifted by 1 (determines when carry bit is generated)
        # keep doing it over and over
        # do it until you dont have a carry -> done
        # o(1) time

        # condition for loop -> until carry value is 0

        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while (b != 0):
            carry = (a & b) << 1
            a = (a ^ b) & mask # a = a xor b -> no carry
            b = carry & mask # b = og a & b -> the and takes care of the carry
        
        return a if a <= max_int else ~(a ^ mask)
         
