# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root :
            return None
        if root == p or root == q:
            return root
        lt = self.lowestCommonAncestor(root.left,p,q)
        rt = self.lowestCommonAncestor(root.right,p,q)
        if lt and rt:
            return root
        if lt:
            return lt
        return rt