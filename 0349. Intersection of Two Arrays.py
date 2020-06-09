"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
"""


class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1)&set(nums2))

if __name__ == "__main__":
    nums1 = [4,9,5]
    nums2 = [9,4]
    result = Solution().intersection(nums1,nums2)
    print(result)
