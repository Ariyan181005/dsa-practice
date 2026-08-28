# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.s=[]
        self.pushLeft(root)
    
    def pushLeft(self,root):
        while root:
            self.s.append(root)
            root=root.left

    def next(self):
        """
        :rtype: int
        """
        node=self.s.pop()
        if node.right:
            self.pushLeft(node.right)
        return node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.s)>0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()