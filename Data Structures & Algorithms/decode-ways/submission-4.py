class Solution:
    def numDecodings(self, s: str) -> int:
        # take care of edge cases first
        # at each position figure out how many ways we can decode up to that point

        # look at various cases:
        # 01: 0
        # 10: 1
        # 22: 2 (2,2 or 22)
        # 30: 0
        # if past 26 and has a 0 then we're screwed
        # if starts with 0 we're screwed

        # if first char is a 0 or s is null: immedieely return 0
        if not s or s[0] == "0":
            return 0
        if len(s) == 1: # only 1 way to decode it
            return 1
        
        dp = [0] * len(s)
        dp[0] = 1 # we alreday know its not a 0

        if s[1] == "0":
            # check if its within 26 -> if its 10
            if s[0] == "1" or s[0] == "2":
                dp[1] = 1
            else:
                return 0
        else:
            if 10 <= int(s[0:2]) <= 26:
                dp[1] = 2
            else:
                dp[1] = 1
        
        for n in range(2, len(s)):
            # follow same logic -> instead of s[1] its gonna be s[i]
            # if its not equal to 0 we're gonna look at the number of i-1 + i
            if s[n] == "0":
            # check if its within 26 -> if its 10
                if s[n-1] == "1" or s[n-1] == "2":
                    dp[n] = dp[n-2]
                else:
                    return 0
            else:
                if 10 <= int(s[n-1 : n+1]) <= 26:
                    dp[n] = dp[n-1] + dp[n-2] # we can do this in 2 seperate ways -> 2 digit num and 1 digit num
                else:
                    dp[n] = dp[n-1] # whatever it was before
        
        return dp[-1]

        