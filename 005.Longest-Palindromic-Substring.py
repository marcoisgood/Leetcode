"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""

class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            print("s,i,i",i,i,self.helper(s,i,i))
            print("s,i,i+1",i,i+1,self.helper(s,i,i+1))
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)
            print(res)

        return res

    def helper(self,s,l,r):

        while 0<=l and r < len(s) and s[l]==s[r]:
                l-=1; r+=1
        return s[l+1:r]


if __name__ == "__main__":
    s = "cbbd"
    result = Solution().longestPalindrome(s)
    print(result)
