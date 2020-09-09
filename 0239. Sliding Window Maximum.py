"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

"""
import collections
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums: return []
        if len(nums) < k: return[]
        res = []
        windows = collections.deque()

        for i in range(k):

            while windows and nums[i] >= windows[-1]:
                windows.pop()

            windows.append(i)
        res.append(nums[windows[0]])

        for i in range(k, len(nums)):
            while windows and nums[i] >= nums[windows[-1]]:
                windows.pop()

            if windows and windows[0] <= i-k:
                windows.popleft()

            windows.append(i)
            res.append(nums[windows[0]])
        return res
if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    res = Solution().maxSlidingWindow(nums, k)
    print(res)
