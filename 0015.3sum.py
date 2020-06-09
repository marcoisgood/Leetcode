"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n-2):
            if nums[i] > 0:
                break
            if nums[i]+nums[n-1]+nums[n-2] < 0:
                continue
            if 0 < i and nums[i] == nums[i-1]:
                continue

            l, r = i+1, n-1

            while l < r:
                tmp = nums[i]+nums[l]+nums[r]
                if tmp == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l+1 < r and nums[l] == nums[l+1]:
                        l+=1
                    l+=1
                    while r-1 > l and nums[r] == nums[r-1]:
                        r-=1
                    r-=1
                elif tmp > 0:

                    r -= 1
                else:

                    l += 1

        return ans

if __name__ == "__main__":
    nums = [3,0,-2,-1,1,2]
    result = Solution().threeSum(nums)
    print(result)
