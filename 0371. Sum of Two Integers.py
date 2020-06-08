"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

"""

class Solution:
    def getSum(self, a: int, b: int) -> int:

        temp = 0
        mask = 0xffffffff
        i = 0
        while (b&mask) != 0:
            i+=1
            tmp = a & b
            a = a^b

            b = (tmp << 1)

        
        return a&mask if b > mask else a

if __name__ == "__main__":
    a = -2
    b = 3
    result = Solution().getSum(a,b)
    print(result)
