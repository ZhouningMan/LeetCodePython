class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.head = None

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        self.stack1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        self.move()
        val = self.stack2.pop()
        return val

    """
    @return: An integer
    """
    def top(self):
        self.move()
        return self.stack2[-1]  # return last element

    def move(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
