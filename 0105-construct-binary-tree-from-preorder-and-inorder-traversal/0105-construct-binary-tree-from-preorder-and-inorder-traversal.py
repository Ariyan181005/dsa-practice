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
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.index = -1
        def build(left, right):
            if left > right:
                return None
            self.index += 1
            val = preorder[self.index]
            node = TreeNode(val)
            mid = inorder_map[val]
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node
        return build(0, len(inorder) - 1)