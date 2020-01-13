def reverse(head):
    if not head:
        return head

    next = head.next
    prev = head
    while next:
        temp = next.next
        next.next = prev
        next = temp
        prev = next
    return prev