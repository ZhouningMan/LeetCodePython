class Solution:
    """
    @param n: the money of you
    @param prices: the price of rice[i]
    @param weight: the weight of rice[i]
    @param amounts: the amount of rice[i]
    @return: the maximum weight
    """
    def backPackVII(self, n, prices, weight, amounts):
        dp = [0] * (n + 1)
        m = len(prices)
        # dp[i][j] is initialized to dp[i-1][j]
        # transition: dp[i][j] = max(dp[i-1][j], dp[i-1][j - k*weight[i-1]] | k <= amounts[i-1])
        # next row depends on previous row.
        for j in range(0, m):  # for each type of item
            for i in reversed(range(1, n + 1)):  # money we have
                for k in range(1, amounts[j] + 1):  # loop through the amount
                    if i - k * prices[j] >= 0:
                        dp[i] = max(dp[i], dp[i - k * prices[j]] + k * weight[j])
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.backPackVII(8, [3,2], [300,160], [1,6]))