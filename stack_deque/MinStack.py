class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, number):
        self.stack.append(number)
        if len(self.min_stack) == 0 or self.min_stack[-1] > number:
            self.min_stack.append(number)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        val = self.stack.pop()
        self.min_stack.pop()
        return val

    def min(self):
        return self.min_stack[-1]