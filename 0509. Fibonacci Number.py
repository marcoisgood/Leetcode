"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).



Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""

class Solution:
    def fib(self, N):
        # # first solution
        # if N == 0: return 0
        # if N == 1: return 1
        # if N == 2: return 1
        #
        # pre, curr = 0, 1
        # for i in range(N):
        #     pre, curr = curr, curr+pre
        #
        # return pre

        # #Second Solution, using dp

        def dp(n, memo):
            if memo[n] != None:
                return memo[n]
            if n == 1 or n == 2:
                return 1
            else:
                memo[n] = dp(n-1, memo) + dp(n-2, memo)
            return memo[n]

        memo = [None for i in range(N+1)]
        memo[0] = 0
        return dp(N, memo)
        
        # # 3. normal recursive:
        # if N == 0: return 0
        # if N == 1: return 1
        #
        # if N > 1:
        #     return self.fib(N-1) + self.fib(N-2)



        # # 4 iterative
        # f = [0, 1]
        # if N == 0:
        #     return f[0]
        # elif N == 1:
        #     return f[1]
        # else:
        #     for i in range(2, N+1):
        #         f.append(f[i-2]+f[i-1])
        # return f[-1]


if __name__ == "__main__":
    N = 4
    result = Solution().fib(N)
    print(result)
