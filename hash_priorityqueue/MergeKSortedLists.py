"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

import heapq

ListNode.__lt__ = lambda x, y: x.val < y.val

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        if not lists:
            return None
        head_items = []
        for li in lists:
            if li:
                heapq.heappush(head_items, li)
        dummy = ListNode(0)
        curr = dummy
        while head_items:
            node = heapq.heappop(head_items)
            curr.next = node
            curr = node
            if node.next:
                heapq.heappush(head_items, node.next)
        return dummy.next

    def mergeKListsRecur(self, lists):
        if not lists:
            return None
        size = len(lists)
        if size == 1:
            return lists[0]
        mid = size // 2
        left = self.mergeKListsRecur(lists[0: mid])
        right = self.mergeKListsRecur(lists[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        if left:
            curr.next = left
        else:
            curr.next = right
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    lists = [ListNode(2, ListNode(4)), None, ListNode(-1)]
    li = s.mergeKListsRecur(lists)
