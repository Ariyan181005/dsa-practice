# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode()
        c=d
        p1=list1
        p2=list2
        while p1 and p2:
            if p2.val>=p1.val:
                c.next=p1
                p1=p1.next
            else:
                c.next=p2
                p2=p2.next
            c=c.next
        if p1:
            c.next=p1
        else:
            c.next=p2
        return d.next