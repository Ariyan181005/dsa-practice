# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, root):
        if root is None:
            return 0, 0
        left_included, left_not_included = self.rec(root.left)
        right_included, right_not_included = self.rec(root.right)
        curr_included = (root.val + left_not_included + right_not_included)
        curr_not_included = max(left_included + right_included,left_included + right_not_included,left_not_included + right_included,left_not_included + right_not_included)
        return curr_included, curr_not_included
    def rob(self, root: TreeNode | None) -> int:
        return max(self.rec(root))