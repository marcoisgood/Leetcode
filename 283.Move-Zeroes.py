
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""
from collections import Counter
class Solution:
    def moveZeroes(self, nums):
        """
        Ans1

        for i in nums:
            if i == 0:
                nums.remove(0)
                nums.append(0)
        return nums
        """
        """
        Ans2
        """
        countzero = nums.count(0)
        nums = [i for i in nums if i != 0]
        nums += [0]*countzero
        return nums


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    result = Solution().moveZeroes(nums)
    print(result)
