# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections 
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q1 = collections.deque()
        q1.append(root)
        q2 = collections.deque()
        label=True
        ret = []
        level = []
        while(len(q1) or len(q2)):
            curQ,nextQ = (q1,q2) if label else (q2,q1)
            node = curQ.popleft()
            if node is None:
                continue
            else:
                level.append(node.val)
                nextQ.append(node.left)
                nextQ.append(node.right)
            if len(curQ) == 0:
                label = not label
                ret.append(level)
                level = []
        return ret