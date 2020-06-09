"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        x=0
        while n != 0:
            print("n: ",n)
            x += n // 5
            print("x: ",x)
            n = n // 5

        return x

if __name__ == "__main__":
    n = 15
    result = Solution().trailingZeroes(n)
    print(result)
