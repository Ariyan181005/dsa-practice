# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dep(n):
            if n is None:
                return 0
            lt=dep(n.left)
            rt=dep(n.right)
            return 1+max(lt,rt)
        return dep(root)