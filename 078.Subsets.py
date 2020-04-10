"""

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""
class Solution:
    def subsets(self, nums):
        res = [[]]
        for j in nums:
            
            res += [i + [j] for i in res]
        return res



if __name__ == "__main__":
    nums = [1,2,3]
    result = Solution().subsets(nums)
    print(result)
