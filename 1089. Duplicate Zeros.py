"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.



Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]

"""

class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """

        if arr.count(0) == 0 or arr.count(0) == len(arr):
            return
        i = 0
        while True:
            if arr[i] == 0:
                if i+1 < len(arr):
                    i+=1
                    arr.insert(i,0)
                    arr.pop()
                else:
                    return
            if i+1 < len(arr):
                i+=1
            else:
                return

if __name__ == "__main__":
    arr = [1,5,2,0,6,8,0,6,0]
    result = Solution().duplicateZeros(arr)
    print(result)
