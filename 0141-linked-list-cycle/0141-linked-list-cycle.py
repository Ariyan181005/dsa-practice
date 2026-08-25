# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        i = head
        j = head
        while j and j.next:
            i = i.next
            j = j.next.next
            if i == j:
                return True
        return False