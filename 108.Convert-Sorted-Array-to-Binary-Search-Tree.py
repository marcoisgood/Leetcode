"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def spreadBST(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end)//2
        root = TreeNode(nums[mid])
        root.left = self.spreadBST(nums, start, mid-1)
        root.right = self.spreadBST(nums, mid+1, end)
        return root

    def sortedArrayToBST(self, nums):
        return self.spreadBST(nums, 0, len(nums)-1)

if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    result = Solution().sortedArrayToBST(nums)
    print(result)
