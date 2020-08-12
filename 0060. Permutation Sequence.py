"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""

class Solution:
    def getPermutation(self, n, k):
        res = ''
        nums = [str(i) for i in range(1, n+1)]

        def helper(n):
            count = 1
            for i in range(2, n+1):
                count*=i

            return count

        while nums:
            n = len(nums) - 1
            combination = helper(n)

            index = 0
            while k > combination:
                index+=1
                k-=combination

            res += nums.pop(index)

        return res



if __name__ == "__main__":
    n = 4
    k = 9
    res = Solution().getPermutation(n,k)
    print(res)
