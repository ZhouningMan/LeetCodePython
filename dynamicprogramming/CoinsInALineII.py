class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        if not values:
            return False
        n = len(values)
        if n < 3:
            return True
        dp = [0] * 3
        dp[(n-1) % 3] = values[n-1]
        dp[(n-2) % 3] = values[n-1] + values[n-2]
        for i in reversed(range(n-2)):
            # dp[i] stores the maximum differences starting from position i
            dp[i % 3] = max(values[i] - dp[(i + 1) % 3], values[i] + values[i+1] - dp[(i + 2) %3])
        return dp[0] > 0


    def firstWillWinPrefix(self, values):
        if not values:
            return False
        n = len(values)
        if n < 3:
            return True
        suffix_sum = self.suffix_sum(values)
        dp = [0] * n
        dp[-1] = values[-1]
        dp[-2] = values[-1] + values[-2]
        for i in reversed(range(n-2)):
            # the maximum value at i for an actor is the maximum value of choosing either i or (i and i+1)
            # elements,
            dp[i] = max(values[i] + suffix_sum[i+1] - dp[i+1],  # dp[i+1] is the maximum value of opponent
                        values[i] + values[i+1] + suffix_sum[i+2]-dp[i+2])
        return dp[0] > suffix_sum[0] / 2

    def suffix_sum(self, values):
        ss = [0] * len(values)
        ss[-1] = values[-1]
        for i in reversed(range(len(values) - 1)):
            ss[i] = ss[i+1] + values[i]
        return ss