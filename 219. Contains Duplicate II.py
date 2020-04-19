"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
class Solution:
    def containsNearbyDuplicate(self, nums, k):


        hash_table = {}

        for i in range(len(nums)):
            n = nums[i]
            if n in hash_table:
                if i - hash_table[n] <= k:
                    return True
            hash_table[n] = i

        return False



if __name__ == "__main__":
    nums = [99,99]
    k = 2
    result = Solution().containsNearbyDuplicate(nums, k)
    print(result)
