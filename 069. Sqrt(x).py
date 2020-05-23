"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x

        max = x
        min = 0
        new = x//2

        while new != min:
            if new**2 > x:
                max = new
            elif new**2 < x:
                min = new
            else:
                return new
            new = (min+max)//2

        return new





if __name__ == "__main__":
    x = 8
    result = Solution().mySqrt(x)
    print(result)
