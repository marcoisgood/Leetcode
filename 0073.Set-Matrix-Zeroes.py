"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""

class Solution:
    def setZeroes(self, matrix):

        def setting(index,matrix):

            for i in range(len(matrix)):
                if matrix[i][index[1]] != 0: matrix[i][index[1]] = 0

            for i in range(len(matrix[0])):
                if matrix[index[0]][i] != 0: matrix[index[0]][i] = 0




        """
        Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        width = len(matrix[0])
        index = []
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    index.append([i,j])

        for i in range(len(index)):
            setting(index[i],matrix)

        return matrix

if __name__ == "__main__":
    matrix = [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]

    result = Solution().setZeroes(matrix)
    print(result)
