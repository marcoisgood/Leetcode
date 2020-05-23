"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Solution:
    def isValid(self, s):

        check = []
        count = 0

        if len(s) == 1:
            return False
        elif len(s) == 0:
            return True

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                check.append(s[i])
                count += 1
            elif not check:
                return False
            else:
                strcheck = check.pop()
                if (s[i] == ')' and strcheck != '(' ) or ( s[i] == '}' and strcheck != '{' ) or ( s[i] == ']' and strcheck != '[' ):
                    return False
                else:
                    count -= 1

        if count == 0:
            return True
        
if __name__ == "__main__":
    s = "()[]{}"
    result = Solution().isValid(s)
    print(result)
