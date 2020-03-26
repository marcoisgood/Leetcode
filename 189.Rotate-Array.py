'''Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

'''

class Solution:
    def rotate(self, nums, k):
        Count = k % len(nums)
        nums[:Count],nums[Count:] = nums[-Count:] , nums[:len(nums)-Count]
        return nums

if __name__ == "__main__":
    nums, k = [1,2,3,4,5,6,7], 3
    result = Solution().rotate(nums, k)
    print(result)
