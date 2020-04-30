"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


class Solution:
    def titleToNumber(self, s):
     dic =  {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

        l = len(s)
        array = list(s)
        count = 0
        tmp = 1
        while l != 0:
            count+=tmp*(dic[array.pop()])
            l-=1
            tmp*=26

        return count """
class Solution:
    def titleToNumber(self, s):
        result = 0
        for i in s:
            result = result*26 + (ord(i) - ord('A')+1)
        return result

if __name__ == "__main__":
    s = "AB"
    result = Solution().titleToNumber(s)
    print(result)
