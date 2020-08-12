"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        dp_max = [0 for i in nums]
        dp_min = [0 for i in nums]
        dp_max[0], dp_min[0] = nums[0], nums[0]

        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i]*dp_max[i-1], nums[i], nums[i]*dp_min[i-1])
            dp_min[i] = min(nums[i]*dp_max[i-1], nums[i], nums[i]*dp_min[i-1])


        return max(dp_max)
if __name__ == "__main__":
    nums = [2,3,-2,4]
    res = Solution().maxProduct(nums)
    print(res)
