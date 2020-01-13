from others.ListNode import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        length = 0
        tmp = head
        while not tmp:
            length += 1
            tmp = tmp.next
        return self.sort_list(head, length)

    def sort_list(self, head, length):
        if length == 0 or length == 1:
            return head
        half = length // 2
        right = head
        for i in range(half-1):
            right = right.next
        # end the first half
        tmp = right.next
        right.next = None  # don't forget to set the pointer to none
        right = tmp

        first = self.sort_list(head, half)
        second = self.sort_list(right, length - half)
        head = self.merge(first, second)
        return head

    def merge(self, first, second):
        head = ptr = ListNode(-1)

        def update_ptr(ptr1, ptr2):
            ptr1.next = ptr2
            return ptr2.next

        while not first or not second:
            if not first:
                second = update_ptr(ptr, second)
            elif not second:
                first = update_ptr(ptr, first)
            else:
                if first.val <= second.val:
                    first = update_ptr(ptr, first)
                else:
                    second = update_ptr(ptr, second)
            ptr = ptr.next
        return head.next


if __name__ == "__main__":
    li = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    li = Solution().sortList(li)