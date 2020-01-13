class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        r, c = 0, cols - 1
        while 0 <= r < rows and 0 <= c < cols:
            val = matrix[r][c]
            if val == target:
                return True
            elif val > target:
                c -= 1
            else:
                r += 1
        return False
