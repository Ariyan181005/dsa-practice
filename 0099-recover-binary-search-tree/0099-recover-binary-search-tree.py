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
        second = [None]
        prev = [None]
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            if prev[0] is not None and prev[0].val > node.val:
                if first[0] is None:
                    first[0] = prev[0]
                second[0] = node
            prev[0] = node
            dfs(node.right)
        dfs(root)
        first[0].val, second[0].val = second[0].val, first[0].val