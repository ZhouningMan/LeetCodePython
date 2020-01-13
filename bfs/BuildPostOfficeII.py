from collections import deque
import sys
class Solution:
    """
    @param grid: a 2D grid. build post office II
    @return: An integer
    """
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return -1

        m = len(grid)
        n = len(grid[0])
        dists = [[-1] * n for _ in range(m)]

        houses = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    houses += 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    self.bfs(grid, m, n, dists, set(), houses, r, c)

        min_dist = sys.maxsize
        for r in range(m):
            for c in range(n):
                if dists[r][c] == -1:
                    continue
                min_dist = min(min_dist, dists[r][c])
        return -1 if min_dist == sys.maxsize else min_dist

    def bfs(self, grid, m, n, dists, visited, houses, r, c):
        visited.add((r, c))
        queue = deque([(r, c)])
        count = 0
        dist = 0
        dists[r][c] = 0
        while queue:
            size = len(queue)
            dist += 1
            for i in range(size):
                cr, cc = queue.popleft()  # current row/col
                for nr, nc in self.neighbors(cr, cc, m, n):  # next row, col
                    if (nr, nc) in visited or grid[nr][nc] == 2:
                        continue
                    if grid[nr][nc] == 1:
                        # layering
                        dists[r][c] += dist
                        count += 1
                    else:
                        queue.append((nr, nc))
                    visited.add((nr, nc))
        if count != houses:
            dists[r][c] = -1

    def neighbors(self, r, c, m, n):
        valid = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < m and 0 <= nc < n:
                valid.append((nr, nc))
        return valid

if __name__ == '__main__':
    s = Solution()
    s.shortestDistance([[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]])