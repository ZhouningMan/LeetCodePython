class Solution:
    def numRollsToTarget(self, d, f, target):
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        dp[0][0] = 1
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                for k in range(1, f + 1):
                    if j - k < 0:
                        continue
                    dp[i][j] += dp[i - 1][j - k]
                    dp[i][j] %= 1000000007
        dp[d][target] %= 1000000007
        return dp[d][target]

# space optimization...
class Solution:
    def numRollsToTarget(self, d, f, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, d + 1):
            for j in reversed(range(1, target + 1)):
                for k in range(1, f + 1):
                    if j - k < 0:
                        continue
                    dp[j] += dp[j - k]
                dp[j] %= 1000000007
        dp[target] %= 1000000007
        return dp[target]