class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        if not values:
            return True
        n = len(values)
        if n < 3:
            return True
        # dp[start][end]: the maximum difference the first actor
        # can get for values in [start, end]
        dp = [[0] * n for _ in range(n)]
        for length in range(1, n + 1):
            for start in range(0, n + 1 - length):
                end = start + length - 1
                if start == end:
                    dp[start][end] = values[start]
                    continue
                # their are only two choices to make, so find the optimal one.
                dp[start][end] = max(values[start] - dp[start + 1][end],
                                     values[end] - dp[start][end-1])
        return dp[0][n - 1] >= 0