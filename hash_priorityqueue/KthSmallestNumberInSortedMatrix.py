import heapq

class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        if k <= 0 or not matrix or not matrix[0]:
            raise ValueError(f"matrix = {matrix}, k = {k}")
        rows = len(matrix)
        cols = len(matrix[0])

        if k > rows * cols:
            raise ValueError(f"k = {k} is greater than total numbers {rows * cols}")
        # keep popping the
        min_q = [(matrix[0][0], 0, 0)]
        # for matrix, we need to make sure we are not revisiting the same elements
        visited = {(0, 0)}
        # loop k - 1 times, the min element in the queue is the answer
        for _ in range(k - 1):
            _, row, col = heapq.heappop(min_q)
            if row + 1 < rows and (row + 1, col) not in visited:
                visited.add((row + 1, col))
                heapq.heappush(min_q, (matrix[row + 1][col], row + 1, col))
            if col + 1 < cols and (row, col + 1) not in visited:
                visited.add((row, col + 1))
                heapq.heappush(min_q, (matrix[row][col + 1], row, col + 1))
        return min_q[0][0]