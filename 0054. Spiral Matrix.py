"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution:
    def spiralOrder(self,array):
        if not array: return []
        res = []
        startCol, endCol = 0, len(array[0])-1
        startRow, endRow = 0, len(array)-1
        while startCol <= endCol and startRow <= endRow:
            for col in range(startCol,endCol+1):
                res.append(array[startRow][col])

            for row in range(startRow+1,endRow+1):
                res.append(array[row][endCol])


            for col in reversed(range(startCol,endCol)):
                if startRow == endRow:
                    break
                res.append(array[endRow][col])




            for row in reversed(range(startRow+1, endRow)):
                if startCol == endCol:
                    break
                res.append(array[row][startCol])



            startCol+=1
            startRow+=1
            endCol-=1
            endRow-=1

        return res





if __name__ == "__main__":
    array = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

    # array = [[1,2,3,4],
    #          [5,6,7,8],
    #          [9,10,11,12]]
    result = Solution().spiralOrder(array)
    print(result)
