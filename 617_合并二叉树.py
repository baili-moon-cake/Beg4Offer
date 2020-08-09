# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self.coreFunc(t1,t2)
    def coreFunc(self, t1: TreeNode, t2: TreeNode):
        if t1 or t2:
            newNode = TreeNode()
            t1Val = t1.val if t1 else 0
            t1Left = t1.left if t1 else None
            t1Right = t1.right if t1 else None
            t2Val = t2.val if t2 else 0
            t2Left = t2.left if t2 else None
            t2Right = t2.right if t2 else None
            newNode.left = self.coreFunc(t1Left,t2Left)
            newNode.right = self.coreFunc(t1Right,t2Right)
            newNode.val = t1Val+t2Val
            return newNode
        else:
            return None

