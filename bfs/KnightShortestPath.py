"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import collections


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


DIRECTIONS = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2),
]


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        if not grid or not grid[0]:
            return -1

        queue = collections.deque()
        queue.append((source.x, source.y))
        distance = {(source.x, source.y): 0}
        while queue:
            (x, y) = queue.popleft()
            if x == destination.x and y == destination.y:
                return distance[(x, y)]
            for dr, dc in DIRECTIONS:
                nr = x + dr
                nc = y + dc
                if self.is_valid(nr, nc, distance, grid):
                    distance[(nr, nc)] = distance[(x, y)] + 1
                    queue.append((nr, nc))
        return -1

    def is_valid(self, nr, nc, distance, grid):
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) \
                or grid[nr][nc] == 1 or (nr, nc) in distance:
            return False
        return True
