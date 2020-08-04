# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def calDepthRecursively(root:TreeNode) -> int:
            if root is None:
                return 0
            return max(calDepthRecursively(root.left),calDepthRecursively(root.right))+1
        return calDepthRecursively(root)

