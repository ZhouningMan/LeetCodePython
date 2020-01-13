from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Solution:
    def updateMatrix(self, matrix):
        queue, visited = self.locate_sources(matrix)
        dist_grid = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        dist = 0
        while queue:
            dist += 1
            size = len(queue)
            for i in range(size):
                pos = queue.popleft()
                for nr, nc in self.neighbors(matrix, visited, pos):
                    if matrix[nr][nc] == 1:
                        dist_grid[nr][nc] = dist
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return dist_grid

    def locate_sources(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        queue = deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        return queue, visited

    def neighbors(self, matrix, visited, pos):
        for dirc in DIRECTIONS:
            nr = pos[0] + dirc[0]
            nc = pos[1] + dirc[1]
            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) \
                    and (nr, nc) not in visited:
                yield nr, nc

if __name__ == '__main__':
    s = Solution()
    s.updateMatrix([[0,0,0],
                    [0,1,0],
                    [1,1,1]])
