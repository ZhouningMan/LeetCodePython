class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        n = len(A)
        # 1D array is for optimization
        # general form of transition function:
        # dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]] + V[i-1])
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            for j in reversed(range(1, m + 1)):
                if j - A[i-1] >= 0:
                    dp[j] = max(dp[j], dp[j-A[i-1]] + V[i-1])
        return dp[m]
