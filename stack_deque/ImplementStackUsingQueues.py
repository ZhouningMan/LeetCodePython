from collections import deque

class Stack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.head = None
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.q1.append(x)
        self.head = x

    """
    @return: nothing
    """
    def pop(self):
        while len(self.q1) > 1:
            self.head = self.q1.popleft()
            self.q2.append(self.head)
        self.q1.popleft()
        # we just need to swap both lists.
        self.q1, self.q2 = self.q2, self.q1

    """
    @return: An integer
    """
    def top(self):
        return self.head

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return len(self.q1) == 0
