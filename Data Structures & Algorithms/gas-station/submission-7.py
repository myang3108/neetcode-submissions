class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # diff = diff between gas and cost to travel to a station (amount left)
        # if it dips to negative then we r screwed
        # first see if its possible to go around the world -> sum up all the gas and subtract total cost
        # after that we can start looking for the entry point

        diff = sum(gas) - sum(cost)
        if diff < 0:
            return -1
        
        # now we know that it is possible.
        # sum the diffs and if it goes negative move on -> that is not the start point
        # keep going until we reach the end of the array (we know that there is only 1 correct ans)
        ans = 0
        total = 0
        for n in range(len(gas)):
            total += (gas[n] - cost[n])
            if total < 0:
                # start from the next val
                total = 0
                ans = n + 1
        
        return ans
            