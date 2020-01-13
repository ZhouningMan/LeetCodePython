class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        # meaning of dp[i][j]: maximum coins when popping [i, j] ballons
        # i - 1 is the left boundary and j + 1 is the right boundary
        dp = [[0] * n for _ in range(n)]
        for length in range(1, n + 1):
            for start in range(n + 1 - length):
                end = start + length - 1
                left = 1 if start == 0 else nums[start - 1]
                right = 1 if end == n - 1 else nums[end + 1]
                for mid in range(start, end + 1):
                    last = left * nums[mid] * right  # we have the middle segment
                    if mid < n - 1:  # if mid is not the last element, we have the right segment
                        last += dp[mid + 1][end]
                    if mid > 0:  # if mid is not the first element, we have the left sgement
                        last += dp[start][mid-1]
                    # update global maximum.
                    dp[start][end] = max(dp[start][end], last)
        return dp[0][n - 1]
