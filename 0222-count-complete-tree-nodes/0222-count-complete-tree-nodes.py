# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        l = 0
        r = 0
        lt = root
        rt = root
        while lt:
            l += 1
            lt = lt.left
        while rt:
            r += 1
            rt = rt.right
        if l == r:
            return (1 << l) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)