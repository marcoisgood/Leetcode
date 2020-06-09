"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        if root is None: return []

        res, stack, flag = [], [root], 1
        while stack:
            tmp, stacktmp = [], []
            for node in stack:
                tmp.append(node.val)
                if node.left: stacktmp.append(node.left)
                if node.right: stacktmp.append(node.right)

            res.append(tmp[::flag])
            stack = stacktmp
            flag*=-1
        return res

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().zigzagLevelOrder(root)
    print(result)
