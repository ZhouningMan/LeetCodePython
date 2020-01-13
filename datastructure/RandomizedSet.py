from random import randrange

class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val):
        if val in self.map:
            return False
        self.list.append(val)
        self.map[val] = len(self.list) - 1

    def remove(self, val):
        if val not in self.map:
            return False
        if val == self.list[-1]:
            self.list.pop()
        else:
            idx = self.map[val]
            last_idx = len(self.list) - 1
            # swap the elements
            self.list[idx] = self.list[last_idx]
            self.list.pop()
            self.map[self.list[idx]] = idx
        # if the val is the last element
        del self.map[val]
        return True

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        i = randrange(len(self.list))
        return self.list[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()