"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

class Solution:
    _dp = [0]
    def numSquares(self, n):


        if not n: return 0

        dp = self._dp
        square = []
        for i in range(1,n+1):
            if i*i <= n:
                square.append(i*i)
            else:
                break


        # dp = [0]

        for i in range(len(dp), n+1):
            dp.append(min(1+dp[i-sqr] for sqr in square if sqr <= i))

        return dp[n]
if __name__ == "__main__":
    n = 12
    res = Solution().numSquares(n)
    print(res)
