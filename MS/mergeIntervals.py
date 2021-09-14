class Solution(object):
    def merge(self, intervals):


        intervals.sort()
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            current = intervals[i]
            prev = result[i-1]

            if current[0] <= prev[1] and current not in result:
                prev[1] = current[1]
                result.append(prev)
            else:
                if current not in result:
                    result.append(current)
        return result

    #starting at subarray 1, is the beginning equal to or less than the end of the prev, if so, replace the end prev end with the new end
    #if not merge, move on

Solution.merge("", [[1,4],[0,2],[3,5]])
