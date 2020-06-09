"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.



Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]

"""
# Ans1
# class Solution:
#     def luckyNumbers (self, matrix):
#
#         row = len(matrix)
#         col = len(matrix[0])
#         res = []
#
#         for i in range(row):
#             num = min(matrix[i])
#             index = matrix[i].index(num)
#             maxnum = 0
#             for m in range(row):
#                 maxnum = max(matrix[m][index], maxnum)
#
#             if num == maxnum:
#                 res.append(num)
#
#
#         return res
# Ans2
class Solution:
    def luckyNumbers (self, matrix):
        min_array = [min(r) for r in matrix]
        max_array = [max(l) for l in zip(*matrix)]
        return [r for r in min_array for l in max_array if r == l]

if __name__ == "__main__":
    matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    result = Solution().luckyNumbers(matrix)
    print(result)
