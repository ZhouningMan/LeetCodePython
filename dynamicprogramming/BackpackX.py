class Solution:
    """
    @param n: the money you have
    @return: the minimum money you have to give
    """
    def backPackX(self, n):
        prices = [150, 250, 350]
        dp = [0] * (n + 1)
        for i in range(3):
            for j in range(prices[i], n + 1):
                dp[j] = max(dp[j], dp[j-prices[i]] + prices[i])
        return n - dp[n]
