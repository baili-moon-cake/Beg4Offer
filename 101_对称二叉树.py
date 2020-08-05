# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        bli = []     # 用来存左子树的前序遍历
        fli = []     # 用来存右子树的后序遍历
        if root == None:   # 无根节点
            return True
        if root and root.left == None and root.right == None:  # 只有根节点
            return True

        if root and root.left and root.right:
            self.pre_order(root.left, bli)
            self.post_order(root.right, fli)
            fli.reverse()            # 将后序遍历的列表倒序
            if bli == fli:
                return True
            else:
                return False

    def pre_order(self,root,li):    # 二叉树的前序遍历
        if root:
            li.append(root.val)
            self.pre_order(root.left,li)
            self.pre_order(root.right,li)
        elif root == None:
            li.append(None)

    def post_order(self,root,li):   # 二叉树的后序遍历
        if root:
            self.post_order(root.left,li)
            self.post_order(root.right,li)
            li.append(root.val)
        elif root == None:
            li.append(None)
