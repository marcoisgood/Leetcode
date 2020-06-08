"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

Assuming the sum of array is S, the minimum element of the array is min and minimum number of moves is m.

Each move will increase the sum of array by n – 1. Finally, every element becomes x. So we have:

S + (n – 1) * m = x * n
min + m = x
We got: m = S – n * min
"""
class Solution:
    def minMoves(self, nums):
        return sum(nums)-min(nums)*len(nums)

if __name__ == "__main__":
    nums = [1,2,3]
    result = Solution().minMoves(nums)
    print(result)
