# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.rec_func(root))
    def rec_func(self, root):
        r_unstolen_maxprofit, r_stolen_maxprofit = 0, 0
        l_unstolen_maxprofit, l_stolen_maxprofit = 0, 0
        if root.right:
            r_unstolen_maxprofit, r_stolen_maxprofit = \
                self.rec_func(root.right)
        if root.left:
            l_unstolen_maxprofit, l_stolen_maxprofit = \
                self.rec_func(root.left)
        
        unstolen_maxprofit = max(r_unstolen_maxprofit, r_stolen_maxprofit) + \
            max(l_unstolen_maxprofit, l_stolen_maxprofit)
        stolen_maxprofit = root.val + r_unstolen_maxprofit + l_unstolen_maxprofit
        return unstolen_maxprofit, stolen_maxprofit

