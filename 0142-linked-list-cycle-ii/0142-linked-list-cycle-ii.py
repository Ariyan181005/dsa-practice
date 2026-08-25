# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = head
        j = head
        while j and j.next:
            i = i.next
            j = j.next.next
            if i == j:
                break
        else:
            return None
        i = head
        while i != j:
            i = i.next
            j = j.next
        return i