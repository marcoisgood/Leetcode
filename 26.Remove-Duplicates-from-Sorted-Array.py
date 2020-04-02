class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        nums[:] = sorted(list(set(nums)))
        return len(nums)


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    result = Solution().removeDuplicates(nums)
    print(result)
"""
"""
