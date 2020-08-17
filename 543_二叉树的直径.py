# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxPath=0
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        else:
            self.depthOfBinaryTree(root)
            return self.maxPath-1
    def depthOfBinaryTree(self, root):
        if not root:
            return 0
        else:
            leftDepth = self.depthOfBinaryTree(root.left)
            rightDepth = self.depthOfBinaryTree(root.right)
            self.maxPath = leftDepth+rightDepth+1
            return max(leftDepth,rightDepth)+1
