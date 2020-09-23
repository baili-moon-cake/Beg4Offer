# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None or root.val is None:
            return []
        stack = deque([[root,],])
        signal = True
        while(signal):
            layer_node_list = []
            for node in stack[0]:
                if node.left:
                    layer_node_list.append(node.left)
                if node.right:
                    layer_node_list.append(node.right)
            if layer_node_list:
                stack.appendleft(layer_node_list)
            else:
                signal=False
        return [[node.val for node in _layer] for _layer in stack]