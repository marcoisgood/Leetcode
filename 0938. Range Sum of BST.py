"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.



Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def rangeSumBST(self, root, L, R):
        if not root: return 0
        if root.val > R: return self.rangeSumBST(root.left, L, R)
        if root.val < L: return self.rangeSumBST(root.right, L, R)
        return self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R) + root.val


if __name__ == "__main__":
    root = TreeNode()
    L = 6
    R = 10
    result = Solution().rangeSumBST(root, L, R)
    print(result)
