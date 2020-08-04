# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归解法
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ret = [root.x,]
        if root.left:
            ret += self.preorderTraversal(root.left)
        if root.right:
            ret += self.preorderTraversal(root.right)
        return ret
# 迭代解法
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        q = [root,]
        ret = []
        while(q):
            node = q.pop()
            if not isinstance(node, TreeNode) and node:
                ret.append(node)
                continue
            if node:
                q.append(node.right)
                q.append(node.left)
                q.append(node.val)
        return ret