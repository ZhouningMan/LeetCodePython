class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """

    def firstWillWin(self, n):
        if n == 0:
            return False
        if n < 3:
            return True
        dp = [False] * 3
        # don't forget to initialize the initial value using
        # rolling row as well
        dp[(n - 1) % 3] = dp[(n - 2) % 3] = True
        for i in reversed(range(n - 2)):
            dp[i % 3] = not dp[(i + 1) % 3] or not dp[(i + 2) % 3]
        return dp[0]

    def firstWillWinReverse(self, n):
        if n == 0:
            return False
        if n < 3:
            return True
        dp = [False] * 3
        # don't forget to initialize the initial value using
        # rolling row as well
        dp[0] = dp[1] = True
        for i in range(2, n):
            dp[i % 3] = not dp[(i - 1) % 3] or not dp[(i - 2) % 3]
        return dp[(n-1) % 3]
