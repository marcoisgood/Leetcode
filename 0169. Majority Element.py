"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
from collections import Counter
class Solution:
    def majorityElement(self, nums):

        mjority = len(nums)//2
        hash_map={}
        hash_map = Counter(nums)
        nums = list(set(nums))

        for i in nums:
            if hash_map[i] > mjority:
                return i

if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    result = Solution().majorityElement(nums)
    print(result)
