# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        res=[]
        def dfs(n,p):
            if not n:
                return
            p+=str(n.val)
            if not n.left and not n.right:
                res.append(p)
                return
            p+="->"
            dfs(n.left,p)
            dfs(n.right,p)
        dfs(root,"")
        return res