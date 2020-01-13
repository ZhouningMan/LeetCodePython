class Solution:
    def oddEvenJumps(self, A):
        if not A:
            return 0
        size = len(A)
        indices = list(range(size))
        indices.sort(key=lambda x: A[x])
        ceilingMap = self.buildMap(indices)
        indices.sort(key=lambda x: -A[x])
        floorMap = self.buildMap(indices)

        dpo = [0] * size
        dpe = [0] * size
        dpo[-1] = 1
        dpe[-1] = 1
        for i in range(size - 2, -1, -1):
            if i in ceilingMap:
                dpo[i] = dpe[ceilingMap[i]]
            if i in floorMap:
                dpe[i] = dpo[floorMap[i]]
        return sum(dpo)

    def buildMap(self, indices):
        stack = []
        idxMap = {}
        for v in indices:
            while stack and stack[-1] <= v:
                idxMap[stack.pop()] = v
            stack.append(v)
        return idxMap
