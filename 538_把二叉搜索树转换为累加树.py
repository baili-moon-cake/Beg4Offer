# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        q = collections.deque()
        q.append(root)
        cumulation = 0
        #使用"类似中序遍历"的方式来遍历，只不过是先右节点，再中节点，最后左节点;
        while(len(q)):
            node = q.pop()
            if isinstance(node, tuple) and node is not None:
                node[1].val+= cumulation
                cumulation += node[0]
                continue
            if node:
                q.append(node.left)
                q.append((node.val,node))
                q.append(node.right)
                node.val += cumulation
        return root
        
