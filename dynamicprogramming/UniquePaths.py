class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # dp[r][c] = dp[r-1][c] + dp[r][c-1]
        dp = [0] * n
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[c] = 1
                elif r == 0:
                    dp[c] = dp[c-1]
                elif c == 0:
                    dp[c] = dp[c]
                else:
                    dp[c] = dp[c] + dp[c-1]
        return dp[n-1]

    def uniquePathsOptimize(self, m, n):
        # dp[r][c] = dp[r-1][c] + dp[r][c-1]
        dp = [0] * n
        dp[0] = 1
        for r in range(m):
            for c in range(n):
                if c > 0:
                    dp[c] = dp[c] + dp[c-1]
        return dp[n-1]