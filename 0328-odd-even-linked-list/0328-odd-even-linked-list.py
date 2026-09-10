# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        o=head
        e=head.next
        eh=e
        while e and e.next:
            o.next=e.next
            o=o.next
            e.next=o.next
            e=e.next
        o.next=eh
        return head