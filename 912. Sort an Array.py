"""
Given an array of integers nums, sort the array in ascending order.



Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
"""
# Ans1 merge sort
# class Solution:
#     def sortArray(self,nums):
#         if len(nums) == 1: return nums
#
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         return self.merge_helper(self.sortArray(left), self.sortArray(right))
#
#     def merge_helper(self,left,right):
#         res = [None]*(len(left) + len(right))
#         index = i = j = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 res[index] = left[i]
#                 i+=1
#             else:
#                 res[index] = right[j]
#                 j+=1
#             index+=1
#
#         while i < len(left):
#             res[index] = left[i]
#             i+=1
#         while j < len(right):
#             res[index] = right[j]
#             j+=1
#         return res
# Ans2
# Quick sort
class Solution:
    def sortArray(self,nums):
        if len(nums) <= 1: return nums

        less, greater, base = [], [], nums.pop()

        for i in nums:
            if i < base: less.append(i)
            else: greater.append(i)
        return self.sortArray(less) + [base] + self.sortArray(greater)

if __name__ == "__main__":
    nums = [5,1,1,2,0,0]
    result = Solution().sortArray(nums)
    print(result)
