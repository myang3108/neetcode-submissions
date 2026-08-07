class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort it by end time -> keep the one that ends earliest -> greedy
        # [[1,2], [2,4], [1,4]]
        # keep [1,2] then keep [2,4]
        # if we keep the one that ends earliest (with no overlap) then we can maximize the number of intervals

        intervals = sorted(intervals, key =lambda x : x[1])
        res = []
        res.append(intervals[0])
        print(res)
        print(res[-1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= res[-1][1]:
                res.append(intervals[i])
        
        return (len(intervals) - len(res))

            

        