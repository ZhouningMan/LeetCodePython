from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and not visited[r][c]:
                    count += 1
                    self.bfs(grid, visited, r, c)
        return count

    def bfs(self, grid, visited, row, col):
        queue = deque([(row, col)])
        visited[row][col] = True
        while queue:
            r, c = queue.popleft()
            for dr, dc in DIRECTIONS:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) \
                        and grid[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))