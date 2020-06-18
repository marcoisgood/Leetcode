"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution:
    def partition(self, s):

        def checking(string):
            left = 0
            right = len(string)-1
            while left < right:
                if string[left] != string[right]:
                    return False

                left += 1
                right -= 1
            return True

        def helper(curr, s):
            if (len(s) == 0):
                res.append(curr[:])
                return
            else:
                for i in range(1,len(s)+1):
                    if (checking(s[:i])):
                        helper(curr + [s[:i]], s[i:])
        res = []
        helper([], s)
        return res



if __name__ == "__main__":
    s = "aab"
    result = Solution().partition(s)
    print(result)
