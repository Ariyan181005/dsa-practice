# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head
        while curr:
            if curr.next and curr.val==curr.next.val:
                value=curr.val
                while curr and curr.val==value:
                    curr=curr.next
                prev.next=curr
            else:
                prev=curr
                curr=curr.next
        return dummy.next
