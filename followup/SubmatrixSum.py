class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrixSum(self, matrix):
        if not matrix or len(matrix[0]) == 0:
            return None
        m = len(matrix)
        n = len(matrix[0])
        # How to extend from 1D to 2D, for 2D matrix,
        # condense each row into a single point
        # now to find submatrix, you can use the same techniques of find subarray
        for i in range(m):  # top row
            col_sum = [0] * n
            for j in range(i, m):  # find choices of bottom row
                prefix_sum = 0
                presum_2_col = {0: -1}
                # for 1D array, it takes linear time to find subarray sub, for matrix, it takes
                # O(m) to find the sum of each submatrix since we have one more dimension
                for k in range(n):  # loop through each column
                    col_sum[k] += matrix[j][k]
                    prefix_sum += col_sum[k]
                    if prefix_sum in presum_2_col:
                        return [(i, presum_2_col[prefix_sum] + 1), (j, k)]
                    presum_2_col[prefix_sum] = k
        return None