"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
"""

class Solution:
    def canAttendMeetings(self, intervals):
        if len(intervals) < 2: return True
        intervals.sort(key=lambda x: x[0])
        l,r = 0, 0
        for i in intervals:
            if l == 0 and r == 0:
                l = intervals[0][0]
                r = intervals[0][1]

            elif not i[0] > r:
                return False

            else:
                l = i[0]
                r = i[1]

        return True


if __name__ == "__main__":
    intervals = [[0,30],[5,10],[15,20]]
    result = Solution().canAttendMeetings(intervals)
    print(result)
