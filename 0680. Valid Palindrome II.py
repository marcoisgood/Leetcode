"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True
Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

"""

class Solution:
    def validPalindrome(self, s):
        if s == s[::-1]:
            return True

        left = 0
        right = len(s) - 1

        while s[left] == s[right]:
            left += 1
            right -= 1


        tmp = s[left+1: right +1 ]

        if tmp == tmp[::-1]:
            return True

        tmp = s[left:right]

        if tmp == tmp[::-1]:
            return True

        return False


if __name__ == "__main__":
    s = "abca"
    result = Solution().validPalindrome(s)
    print(result)
