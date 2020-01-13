class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # create an extra element to accommodate  the range
        self.union_find = [i for i in range(n+1)]

    def connect(self, a, b):
        pa = self._find(a)
        pb = self._find(b)
        self.union_find[pa] = pb

    def _find(self, i):
        while self.union_find[i] != i:
            self.union_find[i] = self.union_find[self.union_find[i]]
            i = self.union_find[i]
        return i

    def query(self, a, b):
        return self._find(a) == self._find(b)
