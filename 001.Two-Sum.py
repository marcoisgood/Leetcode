"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution:
    def twoSum(self, nums, target):
        hash_table = {}
        for i in range(len(nums)):
            hash_table[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i]) in hash_table:
                if hash_table[target - nums[i]] != i:
                    return [i, hash_table[target - nums[i]]]

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    result = Solution().twoSum(nums, target)
    print(result)
