from collections import deque

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.buffer = deque()
        self.sum = 0
        self.size = size

    """
    @param: val: An integer
    @return:
    """
    def next(self, val):
        if len(self.buffer) >= self.size:
            self.sum -= self.buffer.popleft()
        self.buffer.append(val)
        self.sum += val
        return self.sum / min(self.size, len(self.buffer))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)