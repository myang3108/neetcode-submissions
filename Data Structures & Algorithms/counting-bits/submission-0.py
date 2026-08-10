class Solution:
    def countBits(self, n: int) -> List[int]:
        # its a dp problem. list out all the ones from 0-8 and then see the pattern
        # we need to do 1 + dp[n- powerof2 which represents the lsbs in front of the msb we are currently looking at ]
        dp = [0] * (n+1)
        highestpowerof2sofar = 1
        for i in range(1, n+1): # go from 1 to n
            if highestpowerof2sofar * 2 == i: # see if we are on a special one
                highestpowerof2sofar = i
            dp[i] = 1 + dp[i-highestpowerof2sofar]
        
        return dp

        