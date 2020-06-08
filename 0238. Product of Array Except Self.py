"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).


"""

class Solution:
    def productExceptSelf(self, nums):
#         output = []
#         for i in range(len(nums)):
#             tmp = 1
#             for j in range(len(nums)):

#                 if i != j:
#                     tmp = tmp*nums[j]

#             output.append(tmp)

#         return output
        output = []
        left, right, res = [1]*len(nums), [1]*len(nums), [1]*len(nums)
        for i in range(1,len(nums)):
            left[i] = nums[i-1]*left[i-1]

        for i in reversed(range(len(nums)-1)):
            right[i] = nums[i+1]*right[i+1]

        for i in range(len(nums)):
            output.append(left[i]*right[i])

        return output

if __name__ == "__main__":
    nums = [1,2,3,4]
    result = Solution().productExceptSelf(nums)
    print(result)
