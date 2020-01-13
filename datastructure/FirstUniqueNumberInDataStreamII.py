class Node:
    def __init__(self, val, prev = None, next = None):
        self.value = val
        self.prev = prev
        self.next = next

class FirstUniqueNumberInDataStreamII:

    def __init__(self):
        # keeping track of all the values we have seen
        self.seen = set()
        self.unique_map = {}
        self.dummy = Node(None)
        self.tail = self.dummy

    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        if num in self.seen:
            self.remove_unique(num)
            return
        self.seen.add(num)
        self.add_to_unique(num)

    def firstUnique(self):
        return self.dummy.next.value

    def add_to_unique(self, num):
        node = Node(num)
        self.unique_map[num] = node
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def remove_unique(self, num):
        if num not in self.unique_map:
            return
        node = self.unique_map[num]
        del self.unique_map[num]
        node.prev.next = node.next
        if node is self.tail: # special case for tail
            self.tail = node.prev
        else:
           node.next.prev = node.prev


# write your code here