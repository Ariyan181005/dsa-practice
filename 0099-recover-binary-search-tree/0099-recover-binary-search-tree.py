# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first = [None]
        sec = [None]
        prev = [None]
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if prev[0] and prev[0].val > node.val:
                if first[0] is None:
                    first[0] = prev[0]
                sec[0] = node
            prev[0] = node
            inorder(node.right)
        inorder(root)
        first[0].val, sec[0].val = sec[0].val, first[0].val