class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, n, target):
        m = len(A)
        # don't initialize the array using the wrong argument
        # reverse the order of the iteration.
        dp = [[[0] * (target + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        # Because we are iterating from 1, we need to be very
        # careful about the inital value of i == 0 or j == 0 or k == 0
        dp[0][0][0] = 1  # this is important.
        for i in range(1, m + 1):
            dp[i][0][0] = 1  # this is important.
            for j in range(1, min(i, n) + 1):
                for k in range(1, target + 1):
                    dp[i][j][k] = dp[i-1][j][k]
                    if k >= A[i - 1]:
                        dp[i][j][k] += dp[i-1][j-1][k - A[i-1]]
        return dp[m][n][target]

if __name__ == '__main__':
    s = Solution()
    s.kSum([1,2,3,4], 2, 5)