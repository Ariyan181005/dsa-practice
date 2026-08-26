# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        a=[]
        def sol(node):
            if node is None:
                return
            a.append(node.val)
            sol(node.left)
            sol(node.right)
        sol(root)
        return a