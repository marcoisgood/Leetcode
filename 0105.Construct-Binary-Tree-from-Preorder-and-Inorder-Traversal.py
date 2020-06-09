"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            rootIndex = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[rootIndex])
            root.left = self.buildTree(preorder, inorder[:rootIndex])
            root.right = self.buildTree(preorder, inorder[rootIndex+1 :])

            return root


if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    result = Solution().buildTree(preorder, inorder)
    print(result)
