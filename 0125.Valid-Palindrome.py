"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

class Solution:
    def isPalindrome(self, s):
        s = [i.lower() for i in s if i.isalnum()]
        return True if s[:] == s[::-1] else False

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    result = Solution().isPalindrome(s)
    print(result)
