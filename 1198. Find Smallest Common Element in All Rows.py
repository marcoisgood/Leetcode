"""
Given a matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.



Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5

"""

class Solution:
    def smallestCommonElement(self, mat):
        if not mat: return -1

        s = set(mat[0])
        for row in mat[1:]:
            tmp = set()
            for ele in s:
                if ele > row[-1]:
                    break
                if ele not in row:
                    tmp.add(ele)

                s = s - tmp
            if not s: return -1

        return min(s)
if __name__ == "__main__":
    mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
    res = Solution().smallestCommonElement(mat)
    print(res)
