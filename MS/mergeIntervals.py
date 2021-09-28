class Solution(object):
    def merge(self, intervals):
        if len(intervals) < 2: return intervals

        results = []
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= end: #merged interval
                end = max(end, intervals[i][1])


            else:
                results.append([start,end]) #add the prev
                start = intervals[i][0]
                end = intervals[i][1]
        results.append([start,end])  #add the current

        return results


Solution.merge("", [[1,3],[2,6],[8,10],[15,18]])
