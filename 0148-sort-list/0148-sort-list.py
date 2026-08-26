# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #hard way
        """
        if not head or not head.next:
            return head
        s=head
        f=head.next
        while f and f.next:
            s=s.next
            f=f.next.next
        mid=s.next
        s.next=None
        lt=self.sortList(head)
        rt=self.sortList(mid)
        dummy=ListNode(0)
        curr=dummy
        while lt and rt:
            if lt.val <= rt.val:
                curr.next=lt
                lt=lt.next
            else:
                curr.next=rt
                rt=rt.next
            curr=curr.next
        if lt:
            curr.next=lt
        if rt:
            curr.next=rt
        return dummy.next
        """
        #easy way
        vals = []
        start = head
        while start!=None:
            vals.append(start.val)
            start = start.next
        vals.sort()
        start = head
        for x in vals:
            start.val = x
            start=start.next
        return head