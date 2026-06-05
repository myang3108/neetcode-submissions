class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        merged = []
        merged.append(intervals[0])

        # [1,3] -> look at [3,5]
        # because the second interval's start is within the first interval's start,end
        # need to make the second vlaue the merged interval end

        for i in range(1, len(intervals)):
            print(merged)
            if intervals[i][0] >= merged[-1][0] and intervals[i][0] <= merged[-1][1] and intervals[i][1] <=  merged[-1][1]:
                continue
            elif intervals[i][0] >= merged[-1][0] and intervals[i][0] <= merged[-1][1] and intervals[i][1] >  merged[-1][1]:
                merged[-1][1] = intervals[i][1]
            else:
                merged.append(intervals[i])
        
        return merged
