class Solution:
    LABEL = "-"
    LAND = "O"
    WATER = "X"
    DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def solve(self, board: List[List[str]]) -> None:
        if not board or len(board[0]) == 1:
            return

        rows = len(board)
        cols = len(board[0])
        edge_rows = [0, rows - 1]
        for r in edge_rows:
            for c in range(cols):
                if board[r][c] == Solution.LAND:
                    self.dfs(board, r, c)

        edge_cols = [0, cols - 1]
        for r in range(rows):
            for c in edge_cols:
                if (board[r][c]) == Solution.LAND:
                    self.dfs(board, r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == Solution.LAND:
                    board[r][c] = Solution.WATER
                if board[r][c] == Solution.LABEL:
                    board[r][c] = Solution.LAND

    def dfs(self, board, visited: list, r, c):
        board[r][c] = Solution.LABEL
        for (dr, dc) in Solution.DIRECTIONS:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]) \
                    and board[nr][nc] == Solution.LAND and not visited[nr][nc]:
                self.dfs(board, visited, nr, nc)
