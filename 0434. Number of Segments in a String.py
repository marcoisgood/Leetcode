"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""

class Solution():
    def countSegments(self,s):
        return len(s.split())

if __name__ == '__main__':
    s = "Hello world, my name is Marco"
    result = Solution().countSegments(s)
    print(result)
