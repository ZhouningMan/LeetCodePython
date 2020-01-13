class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return f"ListNode({self.val}, {self.next})"

    def __hash__(self) -> int:
        return hash((self.val, self.next))

    def __eq__(self, other):
        return (self.val, self.next) == (other.val, other.next)





