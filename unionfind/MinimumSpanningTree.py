'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''

class UnionFind:
    def __init__(self):
        self.parent = {}

    def add(self, key):
        if key not in self.parent:
            self.parent[key] = key

    def union(self, key1, key2):
        self.add(key1)
        self.add(key2)
        p1 = self.find(key1)
        p2 = self.find(key2)
        if p1 != p2:
            self.parent[p1] = p2

    def find(self, key):
        while key != self.parent[key]:
            self.parent[key] = self.parent[self.parent[key]]
            key = self.parent[key]
        return key

    def connected(self, key1, key2):
        return key1 == key2 or \
               (key1 in self.parent and key2 in self.parent and self.find(key1) == self.find(key2))


class Connection:
    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost

    def __str__(self):
        return f"[{self.city1}, {self.city2}, {self.cost}]"

    # used by print list of connections
    def __repr__(self):
        return f"[{self.city1}, {self.city2}, {self.cost}]"

class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        vertices = set()
        for c in connections:
            vertices.add(c.city1)
            vertices.add(c.city2)

        connections.sort(key=lambda conn: (conn.cost, conn.city1, conn.city2))
        mst = []
        uf = UnionFind()
        for connection in connections:
            if uf.connected(connection.city1, connection.city2):
                continue
            uf.union(connection.city1, connection.city2)
            mst += [connection]
            if len(mst) == len(vertices) - 1:
                break

        if len(mst) != len(vertices) - 1:
            # this is not a spanning tree if the
            # might be a spanning forests
            return []
        return mst


if __name__ == '__main__':
    s = Solution()
    connections = [
        Connection("Acity", "Bcity", 1),
        Connection("Acity", "Ccity", 2),
        Connection("Bcity", "Ccity", 3)
    ]
    print(s.lowestCost(connections))