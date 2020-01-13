DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

class Solution:
    def getMaximumGold(self, grid) -> int:
        # TODO validation
        rows = len(grid)
        cols = len(grid[0])
        gold = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    gold = max(gold, self.dfs(grid, (r, c), set()))
        return gold

    def dfs(self, grid, pos, visited):
        visited.add(pos)
        gold = 0
        for nei in self.neighbors(grid, pos):
            if nei in visited:
                continue
            gold = max(gold, self.dfs(grid, nei, visited))
        gold += grid[pos[0]][pos[1]]
        visited.remove(pos)
        return gold

    def neighbors(self, grid, pos):
        for dirc in DIRECTIONS:
            nr = pos[0] + dirc[0]
            nc = pos[1] + dirc[1]
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc]:
                yield (nr, nc)

if __name__ == '__main__':
    s = Solution()
    ans = s.getMaximumGold([[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]])
    print(ans)
