import heapq

class Solution:
    def assignBikes(self, workers, bikes):
        # heap containing (dist, workerIndx, bikeIndex) pairs
        distances = self.createDistQueue(workers, bikes)
        wokerGotBikes = [False] * len(workers)
        bikeTaken = [False] * len(bikes)
        ans = [0] * len(workers)
        for i in range(len(workers)):
            # get the next available bike
            while distances:
                dist, wi, bi = heapq.heappop(distances)
                if not wokerGotBikes[wi] and not bikeTaken[bi]:
                    ans.append(bi)
                    wokerGotBikes[wi] = True
                    bikeTaken[bi] = True
                    break
        return ans

    # mn*logmn
    def createDistQueue(self, workers, bikes):
        pq = []
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                dist = abs(b[1] - w[1]) + abs(b[0] - w[0])
                pq.append((dist, i, j))
        heapq.heapify(pq)
        return pq


LIMIT = 2000

class Solution2:
    def assignBikes(self, workers, bikes):
        dists = [[] for _ in LIMIT]
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                d = abs(b[1] - w[1]) + abs(b[0] - w[0])
                dists[d].append((i, j))
        bikesTaken = [False] * len(bikes)
        ans = [-1] * len(workers)
        for pairs in dists:
            for p in pairs:
                wi = p[0]
                bi = p[1]
                if ans[wi] != -1 or bikesTaken[bi]:
                    continue
                ans[wi] = bi
                bikesTaken[bi] = True
        return ans

