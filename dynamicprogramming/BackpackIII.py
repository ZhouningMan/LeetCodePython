class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIIITLE(self, A, V, m):
        n = len(A)
        # dp[i][j] meaning: maximum value containing i kinds of item with size j backpack
        dp = [0] * (m + 1)
        # transition function:
        # dp[i][j] = max(dp[i-1][j-kA[i-1] + kV[i-1]] | j-kA[i-1] >=0 and k > 0, dp[i][j])
        for i in range(1, n + 1):
            for j in reversed(range(1, m + 1)):
                k = 0
                # there is a lot of redundant computation here once you draw the decision tree.
                while j - k*A[i-1] >= 0:
                    dp[j] = max(dp[j-k*A[i-1]] + k*V[i-1], dp[j])
                    k += 1
        # this implementation is too slow because it runs O(n*m^2)
        # the inner loop takes too much time.
        return dp[m]

    def backPackIII(self, A, V, m):
        n = len(A)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # transition function:
        # dp[i][j] = max(dp[i][j], dp[i][j-A[i-1]] + V[i-1])
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i-1][j]
                if j - A[i-1] >= 0:
                    # what this means is that, once you have taken one item
                    # you can still take an item from the same type
                    # initially, you take zero item for last type, which basically means
                    dp[i][j] = max(dp[i][j], dp[i][j-A[i-1]] + V[i-1])
        return dp[n][m]


    def backPackIII_Space_Optimzied(self, A, V, m):
        n = len(A)
        dp = [0] * (m + 1)
        # transition function:
        # dp[i][j] = max(dp[i][j], dp[i][j-A[i-1]] + V[i-1])
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j - A[i-1] >= 0:
                    # what this means is that, once you have taken one item
                    # you can still take an item from the same type
                    # initially, you take zero item for last type, which basically means
                    dp[j] = max(dp[j], dp[j-A[i-1]] + V[i-1])
        return dp[m]