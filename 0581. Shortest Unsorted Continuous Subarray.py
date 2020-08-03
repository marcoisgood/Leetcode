"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
"""

class Solution:
    def findUnsortedSubarray(self, nums):
        sortednums = sorted(nums)
        start, end = -1, -1
        i = 0

        while i < len(nums):
            if nums[i] != sortednums[i]:
                start = i
                break
            i+=1

        if start == -1: return 0

        i = len(nums) - 1

        while i >= 0:
            if nums[i] != sortednums[i]:
                end = i
                break
            i-=1

        return end - start + 1
if __name__ == "__main__":
    nums = [2,6,4, 8, 10, 9, 15]
    result = Solution().findUnsortedSubarray(nums)
    print(result)
