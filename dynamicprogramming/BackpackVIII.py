class Solution:
    """
    @param n: the value from 1 - n
    @param value: the value of coins
    @param amount: the number of coins
    @return: how many different value
    """

    def backPackVIII(self, n, value, amount):
        limit = self.get_limit(n, value, amount)
        dp = [False] * (limit + 1)
        m = len(value)
        dp[0] = True
        for i in range(m):
            cnt = [0] * (limit + 1)
            for j in range(value[i], limit + 1):
                # do one coin at a time as long as we have enough coin.
                if not dp[j] and dp[j - value[i]] and cnt[j - value[i]] < amount[i]:
                    dp[j] = True
                    print(j)
                    cnt[j] = cnt[j - value[i]] + 1
        count = -1
        for v in dp:
            if v:
                count += 1
        return count



    def backPackVIIITLE(self, n, value, amount):
        limit = self.get_limit(n, value, amount)
        dp = [False] * (limit + 1)
        m = len(value)
        dp[0] = True
        # transition: dp[i][j] = dp[i-1][j] or dp[i-1][j - k*weight[i-1]] | k <= amounts[i-1]
        for j in range(m):  # zero-based
            for i in reversed(range(value[j], limit + 1)):
                if dp[i]:
                    continue
                for k in range(1, amount[j] + 1):
                    prev = i - k*value[j]
                    if prev >= 0:
                        dp[i] = dp[i] or dp[prev]
                    if dp[i]:
                        break
        count = -1
        for v in dp:
            if v:
                count += 1
        return count

    def get_limit(self, n, value, amount):
        s = 0
        for i in range(len(value)):
            s += value[i] * amount[i]
        return min(n, s)

if __name__ == '__main__':
    s = Solution()
    s.backPackVIII(5, [1,4], [2,1])