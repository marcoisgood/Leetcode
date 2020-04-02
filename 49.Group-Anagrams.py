"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""

from collections import Counter
class Solution:
    def groupAnagrams(self, strs):

        """ans1
        output = [[strs[0]]]
        for words in strs[1:]:

            for i in range(len(output)):
                if Counter(words) == Counter(output[i][0]):
                    output[i].append(words)
                    break

                elif i == len(output)-1:
                    output.append([words])
        return output
        """
        """ Ans2 """
        hashmap = {}
        for w in strs:
            key = "".join(sorted(w))
            if key not in hashmap:
                hashmap[key] = [w]
            else:

                hashmap[key].append(w)

        return hashmap.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = Solution().groupAnagrams(strs)
    print(result)
