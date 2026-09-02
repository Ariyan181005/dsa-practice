# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        sl = head
        ft = head
        while ft and ft.next:
            sl = sl.next
            ft = ft.next.next
        prev = None
        while sl:
            nxt = sl.next
            sl.next = prev
            prev = sl
            sl = nxt
        lt = head
        rt = prev
        while rt:
            if lt.val != rt.val:
                return False
            lt = lt.next
            rt = rt.next
        return True