class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 0
        res = ""
        for c in range(len(s)):
            l,r = c, c
            curr = None
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = r - l + 1
                if curr > maxlen:
                    res = s[l:r+1]
                    maxlen = curr
                l -= 1
                r += 1
        

        for c in range(len(s)):
            l,r = c, c + 1
            curr = None
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = r - l + 1
                if curr > maxlen:
                    res = s[l:r+1]
                    maxlen = curr
                l -= 1
                r += 1


        
        return res

        
            
            
