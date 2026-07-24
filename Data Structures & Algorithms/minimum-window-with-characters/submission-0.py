class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # use a hashmap for the final string w/ count of each letter
        # compare to a hashmap of our current window s's letters
        # have a number that is how many of them r valid
        
        from collections import defaultdict

        mpT, mpS = defaultdict(int), defaultdict(int)
        
        for c in t:
            mpT[c] += 1
        
        res = ""
        valid = 0
        l = 0
        minlen = float('inf')
        have = 0

        for r in range(len(s)):

            c = s[r]
            mpS[c] += 1
            if c in mpT and mpS[c] == mpT[c]:
                have += 1

            while have == len(mpT):
                curLen = r-l+1
                if curLen < minlen:
                    res = s[l:r+1]
                    minlen = curLen

                cl = s[l]
                mpS[cl] -= 1
                if cl in mpT and mpS[cl] < mpT[cl]:
                    have -= 1
            
                l += 1

        return res
                

