"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character,
takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""


class Solution:
    def myAtoi(self, str):

        def checking(string):
            res = 0
            for s in string:
                if not s.isdigit(): break
                res = res*10 + int(s)
            return res

        str = str.strip()

        if str == "": return 0

        elif str[0] not in ['+', '-'] and not str[0].isdigit(): return 0

        else:
            if str[0] in ['+','-']:
                sign = str[0]
                res = checking(str[1:])
                return min(res, 2**31) if sign == "+" else max(-res, -(2**31))
            else:
                return min(checking(str), 2**31)



if __name__ == "__main__":
    str = "-91283472332"

    result = Solution().myAtoi(str)
    print(result)
