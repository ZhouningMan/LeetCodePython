class ConnectingGraph2:
    def __init__(self, n):
        # create an extra element to accommodate  the range
        self.union_find = [i for i in range(n+1)]
        self.size = [1] * (n + 1)

    def connect(self, a, b):
        pa = self._find(a)
        pb = self._find(b)
        # only do this when the parent are not the same
        if pa != pb:
            self.union_find[pa] = pb
            self.size[pb] += self.size[pa]

    def _find(self, i):
        while self.union_find[i] != i:
            self.union_find[i] = self.union_find[self.union_find[i]]
            i = self.union_find[i]
        return i

    def query(self, a):
        pa = self._find(a)
        return self.size[pa]