"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.



Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

"""
import collections
class Solution:
    def relativeSortArray(self, arr1, arr2):
        # # 1
        # hashmap = {}
        # for i in arr1:
        #     if i not in hashmap:
        #         hashmap[i] = 1
        #     else:
        #         hashmap[i] += 1
        # res = []
        #
        # for j in arr2:
        #     res+= [j]*hashmap[j]
        #
        # tmp = sorted([i for i in arr1 if i not in arr2])
        # return res + tmp

        # 2
        hashmap = collections.Counter(arr1)
        res = []
        for i in arr2:
            res += [i]*hashmap.pop(i)
        return res + sorted(hashmap.elements())


if __name__ == "__main__":
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    result = Solution().relativeSortArray(arr1, arr2)
    print(result)
