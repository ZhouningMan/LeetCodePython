class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def add(self, key):
        if key not in self.parent:
            self.parent[key] = key
            self.size[key] = 1

    def union(self, key1, key2):
        self.add(key1)
        self.add(key2)
        p1 = self.find(key1)
        p2 = self.find(key2)
        if p1 != p2:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]

    def find(self, key):
        while key != self.parent[key]:
            self.parent[key] = self.parent[self.parent[key]]
            key = self.parent[key]
        return key


class Solution:
    """
    @param ListA: The relation between ListB's books
    @param ListB: The relation between ListA's books
    @return: The answer
    """
    def maximumAssociationSet(self, ListA, ListB):
        m = len(ListA)
        uf = UnionFind()
        for i in range(m):
            uf.union(ListA[i], ListB[i])
        max_parent = max(uf.size.items(), key=lambda item: item[1])[0]

        result = set()
        for i in range(m):
            if uf.find(ListA[i]) == max_parent:
                result.add(ListA[i])
            if uf.find(ListB[i]) == max_parent:
                result.add(ListB[i])
        return list(result)


if __name__ == '__main__':
    s = Solution()
    print(s.maximumAssociationSet(["abc", "abc", "abc"], ["bcd", "acd", "def"]))