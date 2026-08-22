# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def m(lt, rt):
            if lt is None and rt is None:
                return True
            if lt is None or rt is None:
                return False
            if lt.val != rt.val:
                return False
            return m(lt.left, rt.right) and m(lt.right, rt.left)
        return m(root.left, root.right)