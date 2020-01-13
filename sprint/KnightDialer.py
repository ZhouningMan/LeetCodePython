MAPPINGS = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (0, 3, 9),
    5: (),
    6: (0, 1, 7),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6)
}

BASE = 10 ** 9 + 7


class Solution:

    def knightDialer(self, N: int) -> int:
        dp = [[0] * 10 for _ in range(2)]
        for i in range(N):
            for j in range(10):
                if i == 0:
                    dp[i % 2][j] = 1
                    continue
                dp[i % 2][j] = 0
                for nx in MAPPINGS[j]:
                    dp[i % 2][j] += dp[(i - 1) % 2][nx]
                    dp[i % 2][j] %= BASE
        total = 0
        for j in range(10):
            total += dp[(N - 1) % 2][j]
            total %= BASE
        return total

    def knightDialer3(self, N: int) -> int:
        dp = [[0] * 10 for _ in range(N)]
        for i in range(N):
            for j in range(10):
                if i == 0:
                    dp[i][j] = 1
                    continue
                for nx in MAPPINGS[j]:
                    dp[i][j] += dp[(i - 1)][nx]
                    dp[i][j] %= BASE
        total = 0
        for j in range(10):
            total += dp[(N - 1)][j]
            total %= BASE
        return total

    def knightDialer2(self, N: int) -> int:
        total = 0
        memo = {}
        for i in range(10):
            total += self.dfs(i, N, memo)
            total %= BASE
        return total

    def dfs(self, start, N, memo):
        if N == 1:
            return 1
        if (start, N) in memo:
            return memo[(start, N)]
        count = 0
        for nx in MAPPINGS[start]:
            count += self.dfs(nx, N - 1, memo)
        memo[(start, N)] = count
        return count