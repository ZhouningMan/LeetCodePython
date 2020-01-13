class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        if not A:
            return 0
        m = len(A)
        if m < 2:
            return max(A)
        dp = [A[0],  max(A[0:2])]
        for i in range(2, m):
            # the maximum is determined by either robbing a given house or not.
            dp[i % 2] = max(dp[(i - 1) % 2], dp[(i-2) % 2] + A[i])
        return dp[(m-1) % 2]