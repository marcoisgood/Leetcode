"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y+=1

                best = max(best, y-x)

        return best
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    result = Solution().longestConsecutive(nums)
    print(result)
