"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

"""

class Solution:

    # def subarraySum(self, nums, k):
    #     left, right, count = 0, 1, 0
    #
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)+1):
    #             print("i,j:", i,j)
    #
    #             if sum(nums[i:j]) == k:
    #                 print("--------------------------------")
    #                 print("i,j: ", i, j)
    #                 print(nums[i:j])
    #                 print(sum(nums[i:j]))
    #                 print("+1")
    #                 print("--------------------------------")
    #                 count+=1
    #
    #     return count

    def subarraySum(self, nums, k):
        count = 0
        presum = 0
        hash_map={0:1}
        for num in nums:
            presum += num

            if presum - k in hash_map:
                count+=hash_map[presum-k]

            if presum in hash_map:
                hash_map[presum]+=1
            else:
                hash_map[presum] = 1

        return count

if __name__ == "__main__":
    nums = [1,2,3]
    k=3
    result = Solution().subarraySum(nums,k)
    print(result)
