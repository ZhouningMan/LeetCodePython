BASE = 1000000007

class Solution:

    def numOfPlan(self, n, totalProfit, totalCost, a, b):
        dp = [[[0 for _ in totalCost + 1] for _ in totalProfit + 1] for _ in n + 1]

        dp[0][0][0] = 1
        for i in range(n + 1):
            for p in range(totalProfit + 1):
                for c in range(totalCost + 1):
                    if i == 0 and p == 0 and c == 0:
                        dp[i][p][c] = 0
                    elif i == 0 or p == 0 or c == 0:
                        dp[i][p][c] = 0
                        continue

    """
    @param n: The number of cards
    @param totalProfit: The totalProfit
    @param totalCost: The totalCost
    @param a: The profit of cards
    @param b: The cost of cards
    @return: Return the number of legal plan
    """
    def numOfPlan2(self, n, totalProfit, totalCost, a, b):
        return self.dfs(totalProfit, totalCost, a, b, {}, 0, 0, 0)


    def dfs(self, totalProfit, totalCost, a, b, memo, i, profit, cost):
        if cost >= totalCost:
            return 0
        if i == len(a):
            return 1 if profit > totalProfit else 0

        if profit > totalProfit:
            profit = totalProfit + 1

        if (i, profit, cost) in memo:
            return memo[(i, profit, cost)]

        result = 0
        result += self.dfs(totalProfit, totalCost, a, b, memo, i + 1, profit, cost)
        result += self.dfs(totalProfit, totalCost, a, b, memo, i + 1, profit + a[i], cost + b[i])
        result %= BASE
        if profit > totalProfit:
            profit = totalProfit + 1
        memo[(i, profit, cost)] = result
        return result


