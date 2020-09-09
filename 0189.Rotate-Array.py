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

        # #1
        # Count = k % len(nums)
        # nums[:Count],nums[Count:] = nums[-Count:] , nums[:len(nums)-Count]
        # return nums

        #2
        if not nums:
            return []


        n = len(nums)

        if k > n:
            k %= n

        def helper(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
            return nums

        helper(nums, 0, n-1)
        helper(nums, 0, k-1)
        helper(nums, k, n-1)


        return nums

        #3
        # if not nums or k == 0 or len(nums) == 1:
        #     return
        #
        #
        # n = len(nums)
        #
        # if k > n:
        #     k%=n
        # #copy the last k number to tmp
        # tmp = nums[-k:]
        #
        #
        # nums[-(n-k):] = nums[:n-k]
        # nums[:k] = tmp[:]
        
if __name__ == "__main__":
    nums, k = [1,2,3,4,5,6,7], 3
    result = Solution().rotate(nums, k)
    print(result)
