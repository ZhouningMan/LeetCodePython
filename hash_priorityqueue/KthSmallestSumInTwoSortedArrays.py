import heapq

class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        if not A or not B or k < 0:
            raise ValueError("...")
        rows = len(A)
        cols = len(B)
        if k > rows * cols:
            raise ValueError("...")
        min_q = [(A[0] + B[0], 0, 0)]
        visited = {(0, 0)}
        for _ in range(k - 1):
            _, row, col = heapq.heappop(min_q)
            if row + 1 < rows and (row + 1, col) not in visited:
                visited.add((row + 1, col))
                heapq.heappush(min_q, (A[row + 1] + B[col], row + 1, col))
            if col + 1 < cols and (row, col + 1) not in visited:
                visited.add((row, col + 1))
                heapq.heappush(min_q, (A[row] + B[col + 1], row, col + 1))
        return min_q[0][0]