"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        if len(nums) < 2: return nums
        res = []
        hash_table = {}
        #hash_table = Counter(nums)
        for i in range(0, len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]] = 1
            else:
                hash_table[nums[i]] += 1
        print(hash_table)

        hash_table = sorted(hash_table.items(), key=lambda x:x[1], reverse=True)

        for i in hash_table:
            k-=1
            if k >= 0: res.append(i[0])
            else: break
        return res


if __name__ == "__main__":
    nums = [4,1,-1,2,-1,2,3]
    k = 2
    result = Solution().topKFrequent(nums, k)
    print(result)
