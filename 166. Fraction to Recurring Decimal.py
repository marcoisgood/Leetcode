"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

check valid inputs
check sign
append integer part fisrt and dot

use while look to see whatever the infinite loop of number

## use: divmod()=(div, mod), insert("index", object), join()
"""

class Solution:
    def fractionToDecimal(self, numerator,denominator):
        num, den = numerator, denominator
        res = []
        if not num: return "0"
        if not den: return

        if num* den < 0:
            res.append("-")

        num, den = abs(num), abs(den)
        res.append(str(num//den))
        rmd = num % den

        if not rmd:
            return "".join(res)

        res.append(".")
        d = {}
        while rmd:
            if rmd in d:
                res.insert(d[rmd],"(")
                res.append(")")
                break
            d[rmd] = len(res)
            div, rmd = divmod(rmd*10, den)
            res.append(str(div))
        return "".join(res)





if __name__ == "__main__":
    numerator = 10
    denominator = 3
    result = Solution().fractionToDecimal(numerator, denominator)
    print(result)
