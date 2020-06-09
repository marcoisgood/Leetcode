"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    def generateParenthesis(self, n):
        if not n: return []

        res = []

        self.helper(n,n,'',res)
        return res
    def helper(self, l, r, item, res):
        if r > l: return

        if r == 0 and l == 0:
            return res.append(item)

        if l > 0:
            self.helper(l-1, r, item+'(', res)
        if r > 0:
            self.helper(l, r-1, item+')', res)


if __name__ == "__main__":
    n = 3
    result = Solution().generateParenthesis(n)
    print(result)
