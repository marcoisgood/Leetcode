"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _isValidBST(self,root, maxm, minm):
        if root is None:
            return True
        elif root.val >= maxm or root.val <= minm:
            return False

        return self._isValidBST(root.left, root.val, minm) and self._isValidBST(root.right, maxm, root.val)

    def isValidBST(self, root):
        return self._isValidBST(root, 2147483647.1, -2147483648.1)


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    result = Solution().isValidBST(root)
    print(result)
