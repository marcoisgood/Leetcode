"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution:
    def permuteUnique(self, nums):
        if not len(nums):
            return []

        res = []
        self.helper(nums,[],res)
        return res

    def helper(self, nums, tmp, res):

        if not nums and tmp:
            res.append(tmp)
        else:
            checkbox = set()
            for i in range(len(nums)):
                if nums[i] not in checkbox:
                    self.helper(nums[:i]+nums[i+1:], tmp+[nums[i]], res)
                    checkbox.add(nums[i])

if __name__ == "__main__":
    nums = [1,1,2]
    result = Solution().permuteUnique(nums)
    print(result)
