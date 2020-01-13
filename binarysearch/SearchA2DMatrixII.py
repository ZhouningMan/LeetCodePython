class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        r = rows - 1
        c = 0
        count = 0
        while r >= 0 and c < cols:
            if matrix[r][c] == target:
                count += 1
                r -= 1
                c += 1
            elif matrix[r][c] > target:
                r -= 1
            else:
                c += 1
        return count