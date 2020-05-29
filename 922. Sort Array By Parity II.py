"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.



Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""

class Solution:
    def sortArrayByParityII(self, A):
        nums = [None]*len(A)
        even = 0
        odd = 1

        for i in A:
            if i%2==0:
                nums[even]=i
                even+=2
            else:
                nums[odd]=i
                odd+=2
        return nums


if __name__ == "__main__":
    A = [4,2,5,7]
    result = Solution().sortArrayByParityII(A)
    print(result)
