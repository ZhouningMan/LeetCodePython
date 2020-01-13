from collections import deque

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            raise ValueError("Invalid input....")
        if grid[0][0]:
            return -1
        n = len(grid)
        if n == 1:
            return 1  # special case
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        steps = 1
        while queue:
            size = len(queue)
            # in this case I need to increment the steps here
            # just walk an example to understand
            steps += 1
            for i in range(size):
                pos = queue.popleft()
                for np in self.neightbors(pos, n, grid, visited):
                    if np == (n - 1, n - 1):
                        return steps
                    # don't foget to add the np to the visited set
                    visited.add(np)
                    queue.append(np)
        return -1

    def neightbors(self, pos, n, grid, visited):
        for dirc in DIRECTIONS:
            nx = pos[0] + dirc[0]
            ny = pos[1] + dirc[1]
            # there are three conditions
            # valid point in terms of boundary
            # not visited
            # semantic valid, I fogot to check grid[nx][ny]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or grid[nx][ny] or (nx, ny) in visited:
                continue
            yield (nx, ny)


