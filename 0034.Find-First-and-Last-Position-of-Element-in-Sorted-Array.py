class Solution:
    def searchRange(self, nums, target):

        if target not in nums: return [-1, -1]
        elif len(nums) == 1: return [0, 0]

        index = nums.index(target)
        res = []
        res.append(index)
        index+=1

        while index+1 < len(nums) and nums[index] == target:
            index+=1

        if index+1 == len(nums) and nums[index] == target: res.append(index)

        else: res.append(index-1)

        return res

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    result = Solution().searchRange(nums,target)
    print(result)
