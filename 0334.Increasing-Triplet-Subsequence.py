"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k

Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
Example 1:
Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false

"""

class Solution:
    def increasingTriplet(self, nums):
        if len(nums) < 3: return False
        first = second = float('inf')
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    result = Solution().increasingTriplet(nums)
    print(result)
