"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
"""
# ans 1
# class Solution:
#     def findPeakElement(self, nums):
#         if not nums or len(nums) == 1:
#             return 0
#         if len(nums) == 2:
#             return nums.index(max(nums))
#
#         for i in range(len(nums)):
#             peak = nums[i]
#             if i == 0:
#                 if peak > nums[i+1]:
#                     return i
#             elif i == len(nums) - 1:
#                 if peak > nums[i-1]:
#                     return i
#             else:
#                 if peak > nums[i-1] and peak > nums[i+1]:
#                     return i
#         return 0

class Solution:
    def findPeakElement(self, nums):
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid
        return l

if __name__ == "__main__":
    nums = [1,2,1,3,5,4,4]
    result = Solution().findPeakElement(nums)
    print(result)
