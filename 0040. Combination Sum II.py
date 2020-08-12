"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        n = len(candidates)

        def backtracking(first = 0, path = [], remain = target):

            if remain == 0:
                res.append(path)
                return

            for i in range(first, n):
                if i > first and candidates[i] == candidates[i-1]:
                    continue
                elif candidates[i] > remain:
                    return
                backtracking(i+1, path+[candidates[i]], remain-candidates[i])

        backtracking()
        return res

if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    res = Solution().combinationSum2(candidates, target)
    print(res)
