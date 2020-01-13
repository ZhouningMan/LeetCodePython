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

    def __repr__(self):
        return str(self.val)

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # even if they don't have a intersection,
        # both list will travel the same distance,
        # they will meet at None or the join
        p1 = headA
        p2 = headB
        while p1 is not p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1

if __name__ == '__main__':
    # l1 = ListNode(7, ListNode(8, ListNode(9, ListNode(10, ListNode(11, ListNode(12, ListNode(13)))))))
    # l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, l1))))))
    l2 = None
    l1 = ListNode(1, l2)
    s = Solution()
    ans = s.getIntersectionNode(l1, l2)
    print(ans.val)