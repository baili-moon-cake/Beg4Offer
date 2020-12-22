# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        l2r_stack, r2l_stack = deque([root]), deque()
        ret = []
        while(len(l2r_stack)>0 or len(r2l_stack)>0):
            tmp = []
            if len(l2r_stack) > 0:
                while(len(l2r_stack)>0):
                    node = l2r_stack.pop()
                    r2l_stack.extend(
                        [
                            node for node in [node.left, node.right]
                            if node is not None
                        ]
                    )
                    tmp.append(node.val)
            else:
                while(len(r2l_stack)>0):
                    node = r2l_stack.pop()
                    l2r_stack.extend(
                        [
                            node for node in [node.right, node.left]
                            if node is not None
                        ]
                    )
                    tmp.append(node.val) 
            ret.append(tmp)
        return ret    

            