class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # we need a sliding window that holds the max length of any 2 elements
        res = 0
        mp = defaultdict(int)
        l = 0
        for r in range(len(fruits)):
            mp[fruits[r]] += 1 # add the fruit to the hashmap
            while len(mp) > 2 and l < len(fruits):
                mp[fruits[l]] -= 1

                if mp[fruits[l]] == 0:
                    del mp[fruits[l]]
                    
                l += 1
            res = max(res, r-l+1)



        return res