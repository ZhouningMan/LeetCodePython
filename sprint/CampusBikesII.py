MAX_INT = 2 ** 31 - 1


class Solution:
    def assignBikes(self, workers, bikes) -> int:
        visited = [False] * len(bikes)
        memo = {}
        return self.dfs(workers, bikes, 0, visited, memo)

    def dfs(self, workers, bikes, wi, visited, memo):
        if wi == len(workers):
            return 0
        bitmask = self.getmask(visited)
        if (wi, bitmask) in memo:
            return memo[(wi, bitmask)]
        minD = MAX_INT
        for i in range(len(bikes)):
            if visited[i]:
                continue
            visited[i] = True
            d = self.distance(workers[wi], bikes[i])
            newD = d + self.dfs(workers, bikes, wi + 1, visited, memo)
            minD = min(minD, newD)
            visited[i] = False
        memo[(wi, bitmask)] = minD
        return minD

    def getmask(self, visited):
        mask = 0
        for i, v in enumerate(visited):
            if v:
                mask |= 1 << i
        return mask

    def distance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

if __name__ == '__main__':
    s = Solution()
    dist = s.assignBikes([[815,60],[638,626],[6,44],[103,90],[591,880]],
                         [[709,161],[341,339],[755,955],[172,27],[433,489]])
    print(dist)