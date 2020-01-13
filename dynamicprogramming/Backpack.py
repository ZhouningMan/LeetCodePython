class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # size and the items are two independent variables.
        dp = [0 for _ in range(m + 1)]
        n = len(A)
        for i in range(1, n + 1):
            # we need to reverse the iteration if we only go with 1d array
            for j in reversed(range(1, m + 1)):
                if j - A[i-1] >= 0:
                    dp[j] = max(dp[j], dp[j-A[i-1]] + A[i-1])
        return dp[m]


if __name__ == '__main__':
    s = Solution()
    s.backPack(10, [3, 4, 8, 5])