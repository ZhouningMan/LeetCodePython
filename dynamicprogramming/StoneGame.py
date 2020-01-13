import sys

class Solution:
    def stoneGame(self, A):
        if not A or len(A) < 2:
            return 0
        alen = len(A)
        dp = [[0 for _ in range(alen)] for _ in range(alen)]
        pre_sum = self.prefix_sum(A)
        for length in range(2, alen + 1):
            for start in range(0, alen + 1 - length):
                end = start + length - 1
                dp[start][end] = sys.maxsize
                for mid in range(start, end):
                    last_sum = pre_sum[end] - pre_sum[start] + A[start]
                    dp[start][end] = min(dp[start][end], last_sum + dp[start][mid] + dp[mid+1][end])
        return dp[0][alen-1]

    def prefix_sum(self, A):
        alen = len(A)
        pre_sum = [0] * alen
        pre_sum[0] = A[0]
        for i in range(alen):
            pre_sum[i] = A[i] + pre_sum[i - 1]
        return pre_sum



    def stoneGame2(self, A):
        if not A or len(A) < 2:
            return 0
        alen = len(A)
        pre_sum = [0] * alen
        pre_sum[0] = A[0]
        for i in range(alen):
            pre_sum[i] = A[i] + pre_sum[i-1]
        return self.dfs(A, 0, alen - 1, pre_sum, {})

    def dfs(self, A, start, end, pre_sum, memo):
        if start >= end:
            return 0
        if (start, end) in memo:
            return memo[(start, end)]
        result = sys.maxsize
        for i in range(start, end):
            left = self.dfs(A, start, i, pre_sum, memo)
            right = self.dfs(A, i + 1, end, pre_sum, memo)
            result = min(left + right + pre_sum[end] - pre_sum[start] + A[start], result)
        print((start, end))
        memo[(start, end)] = result
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.stoneGame([3,4,3])
    print(res)