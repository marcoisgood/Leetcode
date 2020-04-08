"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
Ans1 recursively
"""
class Solution:
    def _recursive(self, root, res):

        if root:
            self._recursive(root.left, res)
            res.append(root.val)
            self._recursive(root.right, res)

    def inorderTraversal(self, root):
        res = []
        self._recursive(root, res)
        return res



"""
Ans2 iteratively

class Solution:
    def inorderTraversal(self, root):

        if not root: return []

        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack: return res

            node = stack.pop()
            res.append(node.val)
            root = node.right
"""

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    result = Solution().inorderTraversal(root)
    print(result)
