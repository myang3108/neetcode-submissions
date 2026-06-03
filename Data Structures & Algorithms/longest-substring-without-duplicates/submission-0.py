class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = 0
        myset = set()


        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[left])
                left+=1

            myset.add(s[r])
            count = max(count, r-left+1)
        
        return count
            