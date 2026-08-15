class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # start at the most filled gas station. then go to the next most filled.
        # base case -> calculate total cost, and if the sum of gas station < total cost then return -1
        gastotal = 0
        maxg = 0
        maxgIndex = 0
        balance = 0
        for i,g in enumerate(gas):
            gastotal += g
            if g > maxg:
                maxg = i

        costtotal = 0
        for c in cost:
            costtotal += c
        
        if costtotal - gastotal > 0:
            return -1
        
        # now we have the most expensive
        # traverse it
        
        res = 0
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0: # we're screwed. go to the next one
                total = 0
                res = i + 1
    
        return res
                
        


        
