class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ##sort all of the intervals by the start time
        # ach time look if the first number of the new one is less than the 
        # last number of the prev one
        # added merged ones to the final

        res = []
        intervals.sort(key=lambda x: x[0]) # sort it in place by start
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]: # need to merge
                if res[-1][1] < intervals[i][1]: 
                    res[-1][1] = intervals[i][1]
                else:
                    continue # curr last one swallows it whole (ex. [[1,4],[2,3]])
            else:
                res.append(intervals[i])
        
        return res
