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
        
        # use the diff as the running total incrementer
        # if our total ever drops to 0 -> we run out of gas
        # start from the next position
    
        res = 0
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0: # we're screwed. go to the next one. this position doesnt work
                total = 0
                res = i + 1 # we know it will work for at least one of them
            # if it never dips below 0 it does work. we just need to find the first case where total goes all the way to the end -> since that will be the ONLY solution
    
        return res
                
        


        
