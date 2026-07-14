class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        count = [0] * 26
        res = 0
        l = 0
        for r in range(len(s)):
            count[ord(s[r]) - 65] += 1
            while (r-l+1) - max(count) > k:
                count[ord(s[l]) - 65] -= 1
                l += 1
            
            res = max(res, r-l+1)

        return res
                
        


        # each window - check the breakdown of which characters are in it
        # most popular character is the one we want to change to
        # check if size of window - number of times most popular shows up > k -> number ofthings we gotta change > k
        # then its invalid


