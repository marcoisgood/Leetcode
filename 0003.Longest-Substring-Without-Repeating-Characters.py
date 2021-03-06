"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        words = ""
        maxlen = 0
        for w in s:
            if w not in words:
                words += w
            else:
                words = words[words.index(w)+1:]+w
            maxlen = max(maxlen,len(words))

        return maxlen

if __name__ == "__main__":
    s = "abcabcbb"
    result =Solution().lengthOfLongestSubstring(s)
    print(result)
