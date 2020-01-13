from collections import deque

DIRECTIONS = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, 1), (2, -1), (1, 2), (1, -2)]

class Solution:
    def minKnightMoves(self, x, y):
        # by taking advantage of symmetry
        x = abs(x)
        y = abs(y)
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        count = 0
        while queue:
            size = len(queue)
            for i in range(size):
                point = queue.popleft()
                if point == (x, y):
                    return count
                for np in self.nextPoints(point, visited):
                    queue.append(np)
                    visited.add(np)
            count += 1
        return count

    def nextPoints(self, point, visited):
        for dir in DIRECTIONS:
            np = (dir[0] + point[0], dir[1] + point[1])
            # wrong direction, we need to move in the positive direction
            if np[0] < -2 or np[1] < -2:
                continue
            if np not in visited:
                yield np

if __name__ == '__main__':
    s = Solution()
    moves = s.minKnightMoves(-172, -110)
    print(moves)