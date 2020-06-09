"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""

class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        # equal partition check
        print("total",total)
        if total % 2 != 0:
            print("False")
            return False

        target = total // 2
        print("target", target)

        dp = [False]*(target + 1)
        dp[0] = True

        for num in nums:
            print("--------")
            print("dp",dp)
            print("--------")
            print("num",num)
            for i in range(target, num-1, -1):
                print("i",i)

                if dp[target]:
                    print("dp[target]",dp[target])
                    return True
                print("dp[i]",dp[i])
                print("dp[i-num]", dp[i-num])
                dp[i] = dp[i] or dp[i-num]
                print("dp[i]",dp[i])
        return dp[target]

if __name__ == "__main__":
    nums = [1,5,11,5]
    result = Solution().canPartition(nums)
    print(result)
