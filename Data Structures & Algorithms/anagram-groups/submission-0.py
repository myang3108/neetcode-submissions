class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        ans = []
        for s in strs:
            newS = ''.join(sorted(s))
            print(newS)
            mp[newS].append(s)
        
        for m in mp:
            ans.append(mp[m])
        return ans