"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oTOc={None:None}
        cur=head
        while cur:
            copy=Node(cur.val)
            oTOc[cur]=copy
            cur=cur.next
        cur=head
        while cur:
            copy=oTOc[cur]
            copy.next=oTOc[cur.next]
            copy.random=oTOc[cur.random]
            cur=cur.next
        return oTOc[head]