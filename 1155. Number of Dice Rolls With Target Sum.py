"""
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.



Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation:
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation:
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation:
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation:
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation:
The answer must be returned modulo 10^9 + 7.

http://gitlinux.net/2019-08-15-(1155)-number-of-dice-rolls-with-target-sum/
"""

class Solution:
    def numRollsToTarget(self, d, f, target):
        # Ans 1, DP-Bottom up
        # Time: O(df*target)
        # Space: O(d*target)
        M = 10**9 + 7
        dp = [[0 for x in range(target+1)] for y in range(d+1)]
        dp[0][0] = 1
        for i in range(1, d+1):
            # it is the i times,
            # Example,
            # i = 1, when we roll the first dice.
            # i = 2, when we roll the second dice
            for j in range(i, target+1):
                # j the total value of dices
                    lp = min(j, f)
                    # limitation of K, either biggest value of dice or j.
                    # example, d = 6, the value only from 1 to 6
                    # k is the possible value of the dice this time

                    for k in range(1, lp + 1):
                        dp[i][j] += dp[i-1][j - k]

        print(dp)
        return dp[d][target] % M





if __name__ == '__main__':
    d = 3
    f = 6
    target = 9
    result = Solution().numRollsToTarget(d, f, target)
    print(result)
