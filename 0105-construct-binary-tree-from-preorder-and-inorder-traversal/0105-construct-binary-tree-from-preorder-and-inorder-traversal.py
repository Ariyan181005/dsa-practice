# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None
        r=preorder[0]
        idx=inorder.index(r)
        lt=self.buildTree(preorder[1:idx+1],inorder[:idx])
        rt=self.buildTree(preorder[idx+1:],inorder[idx+1:])
        root = TreeNode(r)
        root.left = lt
        root.right = rt
        return root