"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        intersec = self.get_intersect(head)
        if intersec is None:
            return None
        p = head
        while p is not intersec:
            p = p.next
            intersec = intersec.next
        return p

    def get_intersect(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return slow
        return None