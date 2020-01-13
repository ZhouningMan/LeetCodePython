class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        if n <= 0:
            return
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        self.dfs(board, n,  0, set(), ans)
        return ans

    def dfs(self, board, n, row, col_chosen, ans):
        if row == n:
            ans.append(self.deepCopy(board))
            return
        for i in range(n):
            if i in col_chosen:
                continue
            col_chosen.add(i)
            board[row][i] = 'Q'
            if self.isValid(board, row, i):
                self.dfs(board, n, row + 1, col_chosen, ans)
            # back track
            col_chosen.remove(i)
            board[row][i] = '.'


    def deepCopy(self, board):
        copy = []
        for row in board:
            copy.append(''.join(row))
        return copy

    def isValid(self, board, row, col):
        left_r = row - 1
        left_c = col - 1
        while left_r >= 0 and left_c >= 0:
            if board[left_r][left_c] == 'Q':
                return False
            left_r -= 1
            left_c -= 1
        right_r = row - 1
        right_c = col + 1
        while right_r >= 0 and right_c < len(board):
            if board[right_r][right_c] == 'Q':
                return False
            right_r -= 1
            right_c += 1
        return True

if __name__ == '__main__':
    s = Solution()
    ans = s.solveNQueens(1)
    print(ans)