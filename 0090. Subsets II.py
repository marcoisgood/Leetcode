"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        n = len(nums)
        res = []

        def backtracking(first = 0, curr = []):
            res.append(curr[:])
            for i in range(first, n):
                if i > first and nums[i] == nums[i-1]:
                    continue
                else:
                    curr.append(nums[i])
                    backtracking(i+1, curr)
                    curr.pop()

        backtracking()

        return res

if __name__ == "__main__":
    nums = [1, 2, 2]
    res = Solution().subsetsWithDup(nums)
    print(res)
