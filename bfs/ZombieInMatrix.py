from collections import deque


class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        visited = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    visited.add((r, c))
        days = 0
        while queue:
            size = len(queue)
            for i in range(size):
                r, c = queue.popleft()
                for nr, nc in self.neighbors(r, c, m, n):
                    if (nr, nc) not in visited and grid[nr][nc] == 0:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        grid[nr][nc] = 1
            # if we have turned people into zombies
            if queue:
                days += 1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    return -1
        return days

    def neighbors(self, r, c, m, n):
        valids = []
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < m and 0 <= nc < n:
                valids.append((nr, nc))
        return valids