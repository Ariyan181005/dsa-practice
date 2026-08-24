"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        lev=[root]
        while lev:
            for i in range(len(lev)-1):
                lev[i].next=lev[i+1]
            lev[-1].next=None
            nxt_lev=[]
            for n in lev:
                if n.left:
                    nxt_lev.append(n.left)
                if n.right:
                    nxt_lev.append(n.right)
            lev=nxt_lev
        return root