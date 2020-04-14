"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

"""

class Solution:
    def lengthOfLIS(self, nums):

        if not nums: return 0
        elif len(nums) == 1: return 1
        dp = [1]*len(nums)

        for i in range(1, len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    if dp[i] <= dp[j]:
                        dp[i] = dp[j]+1

        return max(dp)

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    result = Solution().lengthOfLIS(nums)
    print(result)
