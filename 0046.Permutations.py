"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution:
    def permute(self, nums):
        if not nums: return []
        res = []

        def backtracking(array = nums[:], path = []):
            if not array:
                res.append(path)

            for i in range(len(array)):
                backtracking(array[i+1:]+array[:i], path+[array[i]])

        backtracking()

        return res

if __name__ == "__main__":
    nums = [1,2,3]
    result = Solution().permute(nums)
    print(result)
