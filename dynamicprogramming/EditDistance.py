class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """

    def minDistance(self, word1, word2):
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        m = len(word1)
        n = len(word2)
        # dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1) | A[i - 1] != B[j-1]
        dp = [[0] * (n + 1) for _ in range(2)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i % 2][j] = j
                elif j == 0:
                    dp[i % 2][j] = i
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
                    if word1[i-1] != word2[j-1]:
                        dp[i % 2][j] += 1
                    dp[i % 2][j] = min(dp[(i - 1) % 2][j] + 1, dp[i % 2][j - 1] + 1, dp[i % 2][j])
        return dp[m % 2][n]
