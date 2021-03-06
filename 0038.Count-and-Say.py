"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

"""
class Solution:

    def _count(self, n, prev):
        if n == 1:
            return "1"

        prev = self._count(n-1, prev)

        count, string, tmp = 0, "", prev[0]

        for i in range(len(prev)):
            if prev[i] == tmp:
                count+=1
            else:
                string = string + str(count) + prev[i-1]
                count = 1
                tmp = prev[i]
            if i == len(prev)-1:
                string = string + str(count) + prev [i]
        return string


    def countAndSay(self, n):

        return self._count(n, "")


if __name__ == "__main__":
    n = 4
    result = Solution().countAndSay(n)
    print(result)
