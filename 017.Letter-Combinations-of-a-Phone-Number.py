"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""

class Solution:
    def letterCombinations(self, digits):
        if digits == '': return []

        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        tmp = []
        res = ['']

        for i in digits:
            for j in phone[i]:
                for k in res:
                    tmp.append(k+j)
            res[:] = tmp[:]
            tmp = []

        return res


if __name__ == "__main__":
    digits = '23'
    result = Solution().letterCombinations(digits)
    print(result)
