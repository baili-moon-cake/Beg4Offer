# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cur_node = root
        stack = deque()
        while(cur_node or len(stack)>0):
            while(cur_node):
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            k -= 1
            if k == 0:
                return cur_node.val 
            cur_node = cur_node.right