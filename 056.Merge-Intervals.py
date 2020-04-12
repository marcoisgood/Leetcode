"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

class Solution:
    def merge(self, intervals):
        if not intervals: return []

        elif len(intervals) < 2: return intervals

        intervals.sort(key = lambda x : x[0])

        l, r = intervals[0][0], intervals[0][1]

        res = []

        for i in intervals:
            if not i[0] > r :
                l = min(l, i[0])
                r = max(r,i[1])

            else:
                res.append([l,r])
                l = i[0]
                r = i[1]

        res.append([l,r])

        return res

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    result = Solution().merge(intervals)
    print(result)
