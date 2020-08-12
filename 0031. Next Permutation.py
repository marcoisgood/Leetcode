"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution:
    def nextPermutation(self, nums):
        if len(nums) < 2:
            return nums

        n = len(nums)-1

        #first find the peek in nums
        index = n
        while index > 0:
            if nums[index] > nums[index-1]:
                break
            index-=1

        if index == 0:
            nums.sort()
        else:
            peek = index
            #second the number on the left of the peek is the number we want to swap

            x = peek-1
            #third, look the number from end of nums and the one is greater than number we found from second

            index = n
            while index > 0:
                if nums[index] > nums[x]:
                    break
                index-=1

            y = index
        #swap
            nums[x], nums[y] = nums[y], nums[x]
        #reversed the numbers from the peek

            nums[peek:] = reversed(nums[peek:])

        return nums

if __name__ == "__main__":
    nums = [5,1,1]
    res = Solution().nextPermutation(nums)
    print(res)
