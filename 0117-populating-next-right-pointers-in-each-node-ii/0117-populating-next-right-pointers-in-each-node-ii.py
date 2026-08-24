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
        cur=root
        while cur:
            dummy=Node(0)
            tail=dummy
            while cur:
                if cur.left:
                    tail.next=cur.left
                    tail=tail.next
                if cur.right:
                    tail.next=cur.right
                    tail=tail.next
                cur=cur.next
            cur=dummy.next
        return root