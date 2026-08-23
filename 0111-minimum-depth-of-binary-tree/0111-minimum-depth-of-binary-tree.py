# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        q=[(root,1)]
        while q:
            node,deep=q.pop(0)
            if not node.left and not node.right:
                return deep
            if node.left:
                q.append((node.left,deep+1))
            if node.right:
                q.append((node.right,deep+1))