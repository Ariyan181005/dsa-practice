# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(n,l,h):
            if n is None:
                return True
            if n.val<= l or n.val>= h:
                return False
            return check(n.left,l,n.val) and check(n.right,n.val,h)
        return check(root,float("-inf"),float("inf"))