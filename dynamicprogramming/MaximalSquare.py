class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquareWrongImpl(self, matrix):
        if not matrix and not matrix[0]:
            return 0
        # dp[i][j] = d[i-1][j-1] + 3 if d[i-1][j] ==1 1 and d[i][j-1] == 1
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for c in range(n):
            for r in range(m):
                if c == 0 or r == 0:
                    dp[r][c] = matrix[r][c]
                elif matrix[r-1][c] == 1 and matrix[r][c-1] == 1 and dp[r-1][c-1] > 0:
                    dp[r][c] = dp[r-1][c-1] + 3
                else:
                    dp[r][c] = matrix[r][c]


    def maxSquare(self, matrix):
        if not matrix and not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        # dp[r][c]: represents the length of the square
        # dp[r][c] = min(dp[r-1][c-1] dp[r-1][c], dp[r][c-1]) + 1
        # how do you think about this: you can increase the size of the
        # square either by dragging from the square from [r-1][c-1] to [r][c] dp[r-1][c-1] is min
        # or drag [r-1][c] down to [r][c] if dp[r-1][c] is min, similarly for dp[r][c-1]
        dp = [[0] * n for _ in range(2)]
        side = 0
        for r in range(m):
            for c in range(n):
                if c == 0 or r == 0:
                    dp[r % 2][c] = matrix[r][c]
                elif matrix[r][c] != 0:
                    dp[r % 2][c] = min(dp[(r-1) % 2][c-1], dp[r % 2][c-1], dp[(r-1) % 2][c]) + 1
                else:
                    # when using rolling rows, always remember to reinitialize
                    # values that are not properly initialized 
                    dp[r % 2][c] = 0
                side = max(side, dp[r % 2][c])
        return side * side