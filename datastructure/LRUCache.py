from collections import OrderedDict

class Node:
    def __init__(self, key, val, prev=None, next=None):
        # we need to store key for deletion
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        # initialize a dummy node, this save so much problem of null pointer check
        self.dummy = Node(None, None)
        # initial both tail and head points to the dummy
        self.tail = self.dummy

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key in self.cache:
            ans = self.cache[key].val
            self.move_to_end(key)
            return ans
        else:
            return -1
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key in self.cache:
            self.cache[key].val = value
            self.move_to_end(key)
            return
        # if we don't have room, pop the head
        if len(self.cache) == self.capacity:
            self.pop_head()
        node = Node(key, value)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.cache[key] = node

    def pop_head(self):
        # first node is dummy node, so
        # "real" head is self.head.next
        head = self.dummy.next
        key = head.key
        del self.cache[key]
        self.dummy.next = head.next

        # if head is tail, then we want special treatment
        if head is self.tail:
            self.tail = self.dummy
        else:
            head.next.prev = self.dummy


    # this is the key method
    def move_to_end(self, key):
        node = self.cache[key]
        # if it is already the tail
        if node is self.tail:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

class LRU(OrderedDict):
    def __init__(self, maxsize=128, *args, **kwds):
        self.maxsize=maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        # getting the item from the dictionary
        # doesn't change its location
        val = super().__getitem__(key)
        super().move_to_end(key)
        return val

    def __setitem__(self, key, val):
        # setting an item automatically
        # move the element to the end of thequeu
        super().__setitem__(key, val)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]


if __name__ == '__main__':
    s = LRUCache(1)
    s.set(2, 1)
    ans = []
    ans += [s.get(2)]
    s.set(3, 2)
    ans += [s.get(2)]
    ans += [s.get(3)]
    print(ans)
