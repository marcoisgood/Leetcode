"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
# Ans1
# class Solution:
#     def combinations(self, n, k):
#         res = []
#
#         def backtracking(index = 1, path = [], time = k):
#             if time == 0:
#                 res.append(path)
#                 return
#             for i in range(index, n+1):
#                 backtracking(i+1, path+[i], time-1)
#
#         backtracking()
#         return res
# Ans2
from itertools import combinations

class Solution:
    def combinations(self, n, k):
        return list(combinations(range(1,n+1),k))

if __name__ == "__main__":
    n = 4
    k = 2
    res = Solution().combinations(n,k)
    print(res)
