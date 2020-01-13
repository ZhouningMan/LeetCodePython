class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0
        # dp[i][j] = min(dp[i-1][j] , dp[i][j-1]) + grid[i][j]
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        for r in range(m):
            for c in range(n):
                if c == 0 and r == 0:
                    dp[c] = grid[r][c]
                elif c == 0:
                    dp[c] = dp[c] + grid[r][c]
                elif r == 0:
                    dp[c] = dp[c-1] + grid[r][c]
                else:
                    dp[c] = min(dp[c], dp[c-1]) + grid[r][c]
        return dp[n-1]

if __name__ == '__main__':
    s = Solution()
    s.minPathSum([[1,3,1],
                  [1,5,1],
                  [4,2,1]])