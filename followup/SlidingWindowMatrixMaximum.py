class Solution:
    """
    @param matrix: an integer array of n * m matrix
    @param k: An integer
    @return: the maximum number
    """
    def maxSlidingMatrix(self, matrix, k):
        if not matrix or k == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        if k > m or k > n:
            return 0

        col_sum = [0] * n
        ans = -2**31
        for r in range(m):
            win = 0
            for c in range(n):
                col_sum[c] += matrix[r][c]
                if r >= k:
                    col_sum[c] -= matrix[r-k][c]
                # we don't have enough row, stop accumulating on win
                if r < k - 1:
                    continue
                win += col_sum[c]
                if c >= k:
                    win -= col_sum[c-k]
                # we only want to do comparison when we have a valid window
                if c >= k - 1:
                    ans = max(ans, win)
        return ans


