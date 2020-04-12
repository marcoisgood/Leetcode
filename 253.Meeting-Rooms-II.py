"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

"""
class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals: return 0
        elif len(intervals)<2: return 1

        intervals.sort(key = lambda x: x[0])
        room, tmp = [], []
        index = 0

        for i in intervals:
            if not room:
                room.append(int(i[1]))
            else:
                index = 0
                for j in room:

                    if i[0] >= j:
                        room[room.index(j)]= i[1]

                        break
                    elif i[0] < j and index == len(room)-1:
                        tmp.append(i[1])

                    index += 1

            room+=tmp
            room.sort()
            tmp=[]

            
        return len(room)
if __name__ == "__main__":
    intervals = [[3,18],[7,16],[5,18]]
    result = Solution().minMeetingRooms(intervals)
    print(result)
