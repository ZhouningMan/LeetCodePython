class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [0 for _ in range(cols)]
        dp[0] = 1
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                    continue
                if c > 0:
                    dp[c] = dp[c] + dp[c-1]
        return dp[cols - 1]

if __name__ == '__main__':
    s = Solution()
    s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
