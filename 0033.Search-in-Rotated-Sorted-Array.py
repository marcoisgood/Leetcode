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
        if len(nums) == 1:
            if nums[0] == target: return 0
            else: return -1
        if len(nums) == 2:
            if nums[0] == target: return 0
            elif nums[1] == target: return 1
            else: return -1
        m = (0+len(nums))//2
        if (nums[m]-nums[0])*(nums[m]-nums[-1]) < 0:
            l0, r0 = 0, len(nums)
            while l0 < r0:
                m0 = (l0+r0)//2
                if nums[m0] < target:
                    l0 = m0+1
                else:
                    r0 = m0
            if (l0 < len(nums)) and (nums[l0] == target): return l0
            else: return -1

        l, r = 0, len(nums)
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[l]:
                l = m
            else:
                r = m
        if (nums[l]-target)*(target-nums[l+1]) < 0: return -1

        if target <= nums[-1]:
            l1, r1 = l+1, len(nums)
        else:
            l1, r1 = 0, l
        while l1 < r1:
            m1 = (l1+r1)//2
            if nums[m1] < target:
                l1 = m1+1
            else:
                r1 = m1
        if nums[l1] == target: return l1
        else: return -1


if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    result = Solution().search(nums, target)
    print(result)
