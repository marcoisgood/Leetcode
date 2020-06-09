"""
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

"""

class Solution:
    def gcdOfStrings(self, str1, str2):
        if len(str1) == len(str2):
            return str2
        elif len(str2) > len(str1):
            str1, str2 = str2, str1
        if str2 in str1:
            idx = str1.index(str2)
            return self.gcdOfStrings(str2, str1[idx+len(str2):])
        return ""
if __name__ == "__main__":
    str1 = "ABCABC"
    str2 = "ABC"
    result = Solution().gcdOfStrings(str1, str2)
    print(result)
