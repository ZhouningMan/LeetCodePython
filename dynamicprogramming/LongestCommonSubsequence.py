class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        if not A or not B:
            return 0
        m = len(A)
        n = len(B)
        # dp[i][j]: maximum common subsequence with len i and j sequences
        # dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1|A[i-1] == B[j-1])
        dp = [[0] * (m + 1) for _ in range(2)]

        for i in range(1, m+1):
            for j in range(1, n + 1):
                dp[i % 2][j] = max(dp[(i-1) % 2][j], dp[i % 2][j-1])
                if A[i - 1] == B[j - 1]:
                    dp[i % 2][j] = max(dp[i % 2][j], dp[(i - 1) % 2][j - 1] + 1)
        return dp[m % 2][n]