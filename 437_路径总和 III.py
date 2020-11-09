# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
        self.sum = sum
        return self.corefunc(root)[0]


    def corefunc(self, node: TreeNode):
        l_path_sum = r_path_sum = 0
        l_path_list, r_path_list = [], []
        if node.left:
            l_path_sum, l_path_list = self.corefunc(node.left)

        if node.right:
            r_path_sum, r_path_list = self.corefunc(node.right) 
        
        path_sum, path_list = r_path_sum+l_path_sum, []
        for v in l_path_list+r_path_list:
            _path = v + node.val
            path_list.append(_path)
            if _path == self.sum:
                path_sum += 1
        if node.val == self.sum: 
            path_sum += 1
        path_list.append(node.val)
        return  path_sum, path_list