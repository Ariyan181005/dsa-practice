# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if head is None or head.next is None or head.next.next is None:
            return [-1,-1]
        ft=-1
        lt=-1
        prev=head
        curr=head.next
        pos=1
        mn=float('inf')
        while curr.next:
            nxt=curr.next
            if (prev.val < curr.val > nxt.val) or (prev.val > curr.val < nxt.val):
                if ft==-1:
                    ft=pos
                else:
                    mn=min(mn,pos-lt)
                lt=pos
            prev = curr
            curr = nxt
            pos += 1
        if ft == -1 or ft == lt:
            return [-1,-1]
        mx = lt - ft
        return [mn,mx]
