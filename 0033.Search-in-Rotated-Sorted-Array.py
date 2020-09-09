"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

        #return nums.index(target) if target in nums else -1
class Solution:
    def search(self, nums, target):
         if not nums:
            return -1


        l,r =0,len(nums)-1
        while l<=r:
            m = (r+l)//2

            if nums[m]==target: # found the target element
                return m
            elif nums[m]<=nums[r]:  #right-side array is sorted
                # checking for existence of target
                if target>nums[m] and target<=nums[r]:
                    l=m+1
                else: #element won't exist, go to left side array
                    r=m-1
            else: #if right-side is not sorted then left side will be sorted definitely
                # checking for existence of target
                if target>=nums[l] and target<nums[m]:
                    r=m-1
                else: #element won't exist, go to right side
                    l=m+1
        return -1 #didn't find the target


if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    result = Solution().search(nums, target)
    print(result)
