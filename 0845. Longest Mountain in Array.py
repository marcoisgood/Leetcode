"""

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
"""

class Solution:
    def longestMountain(self, A):
        if not A: return 0
        res = 0
        for i in range(1, len(A)-1):
            if A[i-1] < A[i] > A[i+1]:
                l = r = i
                while l and A[l-1] < A[l]: l-=1
                while r+1 < len(A) and A[r+1] < A[r]: r+=1
                tmp = r - l + 1
                if tmp > res: res = tmp
        return res
    
if __name__ == "__main__":
    A = [2,1,4,7,3,2,5]
    result = Solution().longestMountain(A)
    print(result)
