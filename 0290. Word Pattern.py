"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
"""

class Solution:
    def wordPattern(self, pattern, str):
        word = str.split(" ")
        if len(word) != len(pattern):
            return False

        hash_map = {}
        for i in range(len(word)):
            if pattern[i] not in hash_map.keys():
                if word[i] not in hash_map.values():
                    hash_map[pattern[i]] = word[i]
                else:
                    return False

            else:
                if hash_map[pattern[i]] != word[i]:
                    return False

        return True


if __name__ == "__main__":
    pattern = "abba"
    str = "dog cat cat dog"
    res = Solution().wordPattern(pattern, str)
    print(res)
