# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        def build(st,end):
            if st>end:
                return [None]
            a=[]
            for i in range(st,end+1):
                lt=build(st,i-1)
                rt=build(i+1,end)
                for l in lt:
                    for r in rt:
                        root=TreeNode(i)
                        root.left=l
                        root.right=r
                        a.append(root)
            return a
        return build(1,n)