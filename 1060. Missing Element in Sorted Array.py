"""
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.



Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation:
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation:
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation:
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
"""

class Solution:
    def missingElement(self, nums, k):
        maxnum = max(nums)
        tmp2 = tmp = 0

        for i in range(1, len(nums)):
            tmp = tmp + (nums[i]-nums[i-1]-1)
            if tmp >= k:
                return nums[i-1]+k-tmp2

            tmp2 = tmp

        return maxnum + k - tmp

if __name__ == "__main__":
    nums = [4,7,9,10]
    k = 3
    result = Solution().missingElement(nums, k)
    print(result)
