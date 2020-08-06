class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        preorderTraversal_list = self.preorderTraversal(root)
        postorderTraversal_list = self.postorderTraversal(root)
        print([node.val for node in preorderTraversal_list])
        print([node.val for node in postorderTraversal_list])
        commonAncestor = None
        for preorderTraversal,postorderTraversal in zip(preorderTraversal_list,postorderTraversal_list[::-1]):
            if preorderTraversal.val==postorderTraversal.val:
                commonAncestor = preorderTraversal
            if preorderTraversal.val == p.val or preorderTraversal.val == q.val:
                return preorderTraversal
            if postorderTraversal.val == p.val or postorderTraversal.val == q.val:
                return postorderTraversal
        return commonAncestor

    def preorderTraversal(self,root):
        ret = []
        if not root:
            return []
        else:
            ret.append(root)
            ret += self.preorderTraversal(root.left)
            ret += self.preorderTraversal(root.right)
            return ret
    def postorderTraversal(self,root):
        ret = []
        if not root:
            return []
        else:
            ret += self.preorderTraversal(root.left)
            ret += self.preorderTraversal(root.right)
            ret.append(root)
            return ret