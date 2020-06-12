"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation:
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
"""
class Solution:
    def countCharacters(self, words, chars):
        # chars = ''.join(sorted(chars))
        res = 0
        for word in words:
            tmp = chars
            flag = True
            for i in range(len(word)):
                if word[i] in tmp:
                    tmp = tmp.replace(word[i],"",1)
                else:
                    flag = False
                    break
            if flag == True:
                res += len(word)

        return res

if __name__ == '__main__':
    chars = "atach"
    words = ["cat","bt","hat","tree"]
    result = Solution().countCharacters(words, chars)
    print(result)
