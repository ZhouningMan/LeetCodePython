class Solution:
    """
    @param n: Your money
    @param prices: Cost of each university application
    @param probability: Probability of getting the University's offer
    @return: the  highest probability
    """
    def backpackIX(self, n, prices, probability):
        m = len(prices)
        # dp[i] means min probability of all school rejection
        # transition function dp[i][j] = min(dp[i-1][j], dp[i-1][j-prices[i]] * (1 - probability[i])
        dp = [1] * (n + 1)
        for i in range(m):  # loop through schools
            for j in reversed(range(prices[i], n + 1)):  # loop through money
                dp[j] = min(dp[j], dp[j - prices[i]] * (1 - probability[i]))
        return 1.0 - min(dp)
