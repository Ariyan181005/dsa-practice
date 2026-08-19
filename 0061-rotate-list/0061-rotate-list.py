# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        l=1
        tail=head
        while tail.next:
            l+=1
            tail=tail.next
        k=k%l
        if k==0:
            return head
        curr=head
        for i in range(l-k-1):
            curr=curr.next
        nHead=curr.next
        curr.next=None
        tail.next=head
        return nHead