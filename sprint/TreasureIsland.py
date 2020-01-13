from collections import deque

TARGET = 'X'
DANGER = 'D'
DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def treasureIsland(grid):
    visited = set()
    visited.add((0, 0))
    queue = deque()
    queue.append((0, 0))
    steps = 0
    while queue:
        steps += 1
        size = len(queue)
        for i in range(size):
            pos = queue.popleft()
            for nei in neighbors(pos, grid, visited):
                if grid[nei[0]][nei[1]] == TARGET:
                    return steps
                visited.add(nei)
                queue.append(nei)
    return -1


def neighbors(pos, grid, visited):
    for dirc in DIRECTION:
        nr = pos[0] + dirc[0]
        nc = pos[1] + dirc[1]
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) \
            and (nr, nc) not in visited and grid[nr][nc] != DANGER:
            yield nr, nc


if __name__ == '__main__':
    ans = treasureIsland([['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']])
    print(ans)