"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) <= 1:
            return "" if not len(strs) else min(strs, key = len)
        longwords = ""
        shortestLength = len(min(strs, key = len))

        for i in range(shortestLength):
            for j in range(1,len(strs)):
                cur = strs[j]
                pre = strs[j-1]
                if cur[i] != pre[i]:
                    return cur[:i]
            longwords = cur[:i+1]

        return longwords

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    result = Solution().longestCommonPrefix(strs)
    print(result)
