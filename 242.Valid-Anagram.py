"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
"""
from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        return True if Counter(s) == Counter(t) else False
        
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    result = Solution().isAnagram(s,t)
    print(result)
