# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
# Note: The algorithm should run in linear time and in O(1) space.
#
# Example 1:
#
# Input: [3,2,3]
# Output: [3]
# Example 2:
#
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

class Solution:
    def majorityElement(self, nums):

        if not nums:
            return []

        c1, c2 = 0, 1
        count1, count2 = 0, 0

        for i in nums:
            if i == c1:
                count1+=1

            elif i == c2:
                count2+=1

            elif count1 == 0:
                c1 = i
                count1 = 1
            elif count2 == 0:
                c2 = i
                count2 = 1
            else:
                count1-=1
                count2-=1

        return [n for n in (c1, c2) if nums.count(n) > len(nums)//3]



if __name__ == "__main__":
    nums = [3,2,3]
    result = Solution().majorityElement(nums)
    print(result)
