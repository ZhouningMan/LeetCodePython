class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = n

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            self.parent[pa] = pb
            self.size -= 1

    def find(self, a):
        while a != self.parent[a]:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

class Solution:

    def validTree(self, n, edges):
        if len(edges) != n -1:
            return False
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        return uf.size == 1
