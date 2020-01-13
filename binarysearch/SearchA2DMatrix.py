class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        size = rows * cols
        start = 0
        end = size - 1
        while start + 1 < end:
            mid = (start + end) // 2
            row = mid // cols
            col = mid % cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                start = mid
            else:
                end = mid
        return matrix[start//cols][start%cols] == target or matrix[end//cols][end%cols] == target
