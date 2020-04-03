"""
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]

"""

class Solution:
    def findMissingRanges(self, nums,lower,upper):
        res = []
        prev = lower-1
        for i in range(len(nums)+1):
            curr =  nums[i] if i < len(nums) else upper+1
            if curr - prev > 1:
                if curr - 1 > prev + 1:
                    res.append(str(prev+1)+ "->" + str(curr-1))
                else:
                    res.append(str(curr-1))
            prev = curr
        return res

if __name__ == "__main__":
    nums = [0, 1, 3, 50, 75]
    lower, upper = 0, 99
    result = Solution().findMissingRanges(nums,lower, upper)
    print(result)
