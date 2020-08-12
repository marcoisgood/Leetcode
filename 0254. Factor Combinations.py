"""
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""

class Solution:
    def getFactors(self, n):

        if n < 4: return []
        res = []
        def backtracking(path, target, time):
            for num in range(2, target+1):
                if num * num > target:
                    return
                if target%num == 0:
                    res.append(path+[num, target//num])
                    backtracking(path+[num], target//num, time+1)


        backtracking([], n, 0)
        return res

if __name__ == "__main__":
    n = 8
    res = Solution().getFactors(n)
    print(res)
