"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root, k):
        dic = {0:1}
        return self.helper(root, k, dic)

    def helper(self, node, target, dic):
        print(dic)

        if not node:
            return



        if target - node.val in dic:
            print("--------")
            print(target - node.val)
            print(dic)
            print("--------")
            print(True)
            return True

        dic[node.val] = 1


        return self.helper(node.left, target,dic) or self.helper(node.right, target,dic)

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    target = 3
    result = Solution().findTarget(root,target)
    print(result)
# [5,3,6,2,4,null,7] 9
# [2,1,3] 3
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str2, str1 = str1, str2


        left, right = 0, 0
        index = 0
        while index < len(str2) and left < len(str1):
            if str2[index] == str1[right]:
                right+=1
                index+=1

            elif str2[index] != str1[right]:

                left+=1
                right = left
                index = 0


        return str1[right:]
"""
