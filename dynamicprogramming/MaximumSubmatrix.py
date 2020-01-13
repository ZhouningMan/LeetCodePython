MIN_INT = -2 ** 31


class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """

    def maxSubmatrix(self, matrix):
        if not matrix or not matrix[0]:
            raise ValueError("....")
        rows = len(matrix)
        cols = len(matrix[0])
        ans = MIN_INT
        for top in range(rows):
            colSum = [0] * cols
            for bot in range(top, rows):
                for i in range(cols):
                    colSum[i] += matrix[bot][i]
                ans = max(ans, self.maxSubarray(colSum))
        return ans

    def maxSubarray(self, array):
        ans = array[0]
        curr = array[0]
        for i in range(1, len(array)):
            curr += array[i]
            curr = max(array[i], curr)
            ans = max(ans, curr)
        return ans


if __name__ == '__main__':
    s = Solution()
    ans = s.maxSubmatrix([
    [1,3,-1],
    [2,3,-2],
    [-1,-2,-3]])
    print(ans)