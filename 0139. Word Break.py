"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

"""

class Solution:
    def wordBreak(self, s,wordDict) :
        # Ans1
        # if len(s) == 0:
        #     return True
        #
        # for word in wordDict:
        #     prefix = s[0:len(word)]
        #     result = False
        #
        #     if prefix == word:
        #         result = self.wordBreak(s[len(word):],wordDict)
        #
        #     if result:
        #         return True
        # return False

        # ans2
        # def helper(s, wordDict, memo):
        #
        #     print("----------------------------------------------------------------")
        #     print("S: ",s)
        #
        #     if len(s) == 0:
        #         return True
        #
        #     elif s in memo:
        #         print("s in memo: ",s )
        #         return memo[s]
        #
        #     for word in wordDict:
        #         print("word: ", word)
        #         if s [0:len(word)] == word and helper(s[len(word):], wordDict, memo):
        #             memo[word] = True
        #             print("True in If: memo and word ",memo, word)
        #             return True
        #
        #     memo[s] = False
        #     print("memo[s] = False: ", memo)
        #     return False
        #
        # memo = {}
        # return helper(s, wordDict, memo)

        #ans3
        dp = [False for i in range(len(s)+1)]
        dp[0] = True

        for i in range(1,len(s)+1):
            for j in range(i-1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]
if __name__ == "__main__":
    # s = "abcdefgh"
    # wordDict = ["ab","cd","abcd","h"]
    # s ="catsandog"
    # wordDict = ["cats","dog","sand","and","cat"]
    s ="abcdef"
    wordDict = ["ab","cd","ef"]
    result = Solution().wordBreak(s, wordDict)
    print(result)
