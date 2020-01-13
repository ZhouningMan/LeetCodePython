"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class UnionFind:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.root = [-1] * (n * m)
        self.count = 0

    def union(self, pos1, pos2):
        if not self.valid(pos1) or not self.valid(pos2):
            return
        parent1 = self.find(pos1)
        parent2 = self.find(pos2)
        if parent1 == -1 or parent2 == -1 or parent1 == parent2:
            return
        self.root[parent1] = parent2
        self.count -= 1

    def find(self, pos):
        if not self.valid(pos):
            return 0

        parent = pos.x * self.m + pos.y
        while self.root[parent] != -1 and self.root[parent] != parent:
            self.root[parent] = self.root[self.root[parent]]  # path compression
            parent = self.root[parent]
        return self.root[parent]

    def add(self, pos):
        if not self.valid(pos):
            return
        parent = pos.x * self.m + pos.y
        if self.root[parent] != -1:
            return
        self.root[parent] = parent
        self.count += 1

    def valid(self, pos):
        return 0 <= pos.x < self.n and 0 <= pos.y < self.m

    def connected(self):
        return self.count

class Solution:

    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def numIslands2(self, n, m, operators):
        result = []
        union_find = UnionFind(n, m)
        for point in operators:
            union_find.add(point)  # add a piece of land
            for direction in Solution.DIRECTIONS:  # connect all adjacent lands together
                neighbor = Point(direction[0] + point.x, direction[1] + point.y)
                union_find.union(point, neighbor)
            print(union_find.root)
            result.append(union_find.connected())
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.numIslands2(3, 3, [Point(0, 0), Point(2, 0)]))