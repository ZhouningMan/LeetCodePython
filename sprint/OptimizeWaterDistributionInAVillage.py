class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        allEdges = self.getEdges(n, wells, pipes)
        allEdges.sort(key=lambda p: p[2])
        # zero is the ground all house has an edge to ground
        uf = UnionFind(n + 1)
        total = 0
        count = 0
        for edge in allEdges:
            s = edge[0]
            t = edge[1]
            if uf.connected(s, t):
                continue
            uf.union(s, t)
            total += edge[2]
            count += 1
            # if it is a tree, the # of edges must be total vertices - 1
            if count == n:
                return total
        return total

    def getEdges(self, n, wells, pipes):
        all = []
        # This is the most important point, every house has a edge to the ground
        for i in range(1, n + 1):
            all.append((0, i, wells[i - 1]))
        all += pipes
        return all


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def union(self, s, t):
        ps = self.find(s)
        pt = self.find(t)
        self.parent[ps] = pt

    def find(self, s):
        while self.parent[s] != s:
            # path compression, set parent to grandparent
            self.parent[s] = self.parent[self.parent[s]]
            s = self.parent[s]
        return s

    def connected(self, s, t):
        return self.find(s) == self.find(t)

