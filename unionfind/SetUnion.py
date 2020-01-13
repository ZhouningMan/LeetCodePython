class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = 0

    def add(self, key):
        if key not in self.parent:
            self.parent[key] = key
            self.size += 1

    def union(self, key1, key2):
        p1 = self.find(key1)
        p2 = self.find(key2)
        if p1 != p2:
            self.parent[p1] = p2
            self.size -= 1

    def find(self, key):
        while key != self.parent[key]:
            self.parent[key] = self.parent[self.parent[key]]
            key = self.parent[key]
        return key


class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def setUnion(self, sets):
        uf = UnionFind()
        for nums in sets:
            for num in nums:
                uf.add(num)
            for i in range(1, len(nums)):
                uf.union(nums[i], nums[i-1])
        union_by_parent = {}
        for nums in sets:
            for num in nums:
                parent = uf.find(num)
                if parent not in union_by_parent:
                    union_by_parent[parent] = set()
                union_by_parent[parent].add(num)
        return uf.size