class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        intervals.sort()
        res.append(intervals[0])
        for x,y in intervals[1:]:
            if res[-1][1] < x:
                res.append([x,y])
            else:
                res[-1][1] = max(res[-1][1], y)
        return res
