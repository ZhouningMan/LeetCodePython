import sys
import collections

DIRECTIONS_DP = [(-2, -1), (2, -1), (-1, -2), (1, -2)]

DIRECTIONS_BFS = [(1, 2), (-1, 2), (2, 1), (-2, 1)]


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        if not grid or not grid[0]:
            return -1
        m = len(grid)
        n = len(grid[0])
        dp = [[sys.maxsize] * 3 for _ in range(m)]
        dp[0][0] = 0
        for c in range(n):
            if c >= 3:
                for r in range(m):
                    # we need reinitialize the new column to max
                    dp[r][c % 3] = sys.maxsize
            for r in range(m):
                # current cell must not be zero
                if grid[r][c]:
                    continue
                for dr, dc in DIRECTIONS_DP:
                    pr, pc = dr + r, dc + c
                    if not self.is_valid(pr, pc, dp, grid):
                        continue
                    dp[r][c % 3] = min(dp[r][c % 3], dp[pr][pc % 3] + 1)
        return -1 if dp[m - 1][(n - 1) % 3] == sys.maxsize else dp[m - 1][(n - 1) % 3]

    def is_valid(self, r, c, dp, grid):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) \
                or dp[r][c % 3] == sys.maxsize:
            return False
        return True

    def shortestPath2BFS(self, grid):
        if not grid or not grid[0]:
            return -1
        m = len(grid)
        n = len(grid[0])
        queue = collections.deque([(0, 0)])
        distance = {(0, 0): 0}

        while queue:
            x, y = queue.popleft()
            if x == m - 1 and y == n - 1:
                return distance[(x, y)]
            for dx, dy in DIRECTIONS_BFS:
                nx, ny = dx + x, dy + y
                if not self.is_valid_bfs(nx, ny, grid, distance):
                    continue
                queue.append((nx, ny))
                distance[(nx, ny)] = distance[(x, y)] + 1
        return -1

    def is_valid_bfs(self, x, y, grid, distance):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) \
                or grid[x][y] == 1 or (x, y) in distance:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    s.shortestPath2([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
