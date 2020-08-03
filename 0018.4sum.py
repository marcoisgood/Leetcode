"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""

class Solution:
    def fourSum(self, nums, target):

        def helper(nums, target, N, result, res):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
                return


            if N == 2:
                l, r = 0 , len(nums)-1
                while l < r:
                    tmp = nums[l] + nums[r]
                    if tmp == target:
                        res.append(result + [nums[l], nums[r]])
                        l+=1
                        while l < r and nums[l] == nums[l-1]:
                             l+=1
                    elif tmp < target:
                        l+=1
                    else:
                        r-=1

            else:
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        helper(nums[i+1:], target-nums[i], N-1, result+[nums[i]], res)

        res = []
        helper(sorted(nums), target, 4, [], res)
        return res


if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    result = Solution().fourSum(nums, target)
    print(result)
