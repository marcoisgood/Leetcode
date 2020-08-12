"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution:
    def generateMatrix(self, n):
        if n == 1: return [[1]]
        if n == 0: return []

        res = [[0 for x in range(n)] for y in range(n)]
        startRow, startCol = 0, 0
        endRow, endCol = n-1, n-1
        num = 1
        target = n*n

        while num < target+1:
            for col in range(startCol,endCol+1):
                res[startRow][col] = num
                num+=1
            for row in range(startRow+1, endRow+1):
                res[row][endCol] = num
                num+=1

            for col in reversed(range(startCol, endCol)):
                if startRow == endRow:
                    break
                res[endRow][col] = num
                num+=1

            for row in reversed(range(startRow+1, endRow)):
                if startCol == endCol:
                    break
                res[row][startCol] = num
                num+=1

            startCol+=1
            startRow+=1
            endCol -= 1
            endRow -= 1

        return res
if __name__ == "__main__":
    n = 3
    result = Solution().generateMatrix(n)
    print(result)
