class Solution(object):
    def minMeetingRooms(self, intervals):
        meetings = []
        maxRooms = 0

        for sub in intervals:
            meetings.append([sub[0], 1])
            meetings.append([sub[1], -1])

        meetings.sort()


        count = 0
        for sub_meeting in meetings:
            count += sub_meeting[1]
            maxRooms = max(count, maxRooms)
        return maxRooms


Solution.minMeetingRooms("", [[13,15],[1,13]])
