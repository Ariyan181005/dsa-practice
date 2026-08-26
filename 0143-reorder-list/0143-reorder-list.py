# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        prev=None
        cur=s.next
        s.next=None
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        f=head
        s=prev
        while s:
            t1=f.next
            t2=s.next
            f.next=s
            s.next=t1
            f=t1
            s=t2