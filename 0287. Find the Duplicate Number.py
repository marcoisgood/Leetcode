"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
"""

class Solution:
    def findDuplicate(self, nums):
        #use Floyd's Algorithm
        #https://www.youtube.com/watch?v=9YTjXqqJEFE

        t, h = nums[0], nums[nums[0]]
        while t != h:
            t, h = nums[t], nums[nums[h]]

        t = 0

        while t != h:
            t, h = nums[t], nums[h]

        return t

if __name__ == "__main__":
    nums = [3,1,3,4,2]
    res = Solution().findDuplicate(nums)
    print(res)
