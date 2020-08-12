"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        def backtracking(path=[], remain = target):
            if remain == 0:
                res.append(path)
                return
            for num in candidates:
                if num > remain:
                    return
                elif path and num < path[-1]:
                    continue

                backtracking(path+[num], remain-num)


        backtracking()
        return res

if __name__ == "__main__":
    candidates = [2,3,5]
    target = 8
    res = Solution().combinationSum(candidates, target)
    print(res)
