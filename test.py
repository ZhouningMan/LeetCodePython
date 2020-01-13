class UnionFind:
    def __init__(self, m):
        self.root = [i for i in range(m)]
        self.connected = 0

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi == pj:
            return
        self.root[pi] = self.root[pj]
        self.connected += 1

    def find(self, i):
        while self.root[i] != i:
            # path compression
            self.root[i] = self.root[self.root[i]]
            i = self.root[i]
        return i


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    def numIslands2(self, m, n, positions):
        size = m * n
        uf = UnionFind(size)
        ans = []
        lands = set()
        for p in positions:
            lands.add((p.x, p.y))
            for nr, nc in self.neighbors(m, n, p.x, p.y):
                if (nr, nc) not in lands:
                    continue
                uf.union(nr * n + nc, p.x * n + p.y)
            ans.append(len(lands) - uf.connected)
        return ans

    def neighbors(self, m, n, r, c):
        for dr, dc in DIRECTIONS:
            nr = dr + r
            nc = dc + c
            if 0<= nr < m and 0 <= nc < n:
                yield nr, nc


