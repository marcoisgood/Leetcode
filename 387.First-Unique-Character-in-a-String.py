"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
from collections import Counter

class Solution:
    def firstUniqChar(self, s):
            if not s: return -1
            hash_table = Counter(s)

            for index, char in enumerate(s):
                if hash_table[char] == 1:
                    return index

            return -1

if __name__ == "__main__":
    s = "loveleetcode"
    result = Solution().firstUniqChar(s)
    print(result)
