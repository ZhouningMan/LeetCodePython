import collections

DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longestContinuousIncreasingSubsequence2(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        size = [[0] * n for _ in range(m)]
        queue = collections.deque()
        result = 1
        # find crests of the matrix which will be used as the
        # starting points of bfs
        for r in range(m):
            for c in range(n):
                if self._is_trough(r, c, m, n, size, matrix):
                    queue.append((r, c))
        # initialize the size of the crests
        # initialize the size outside the the previous for loop which
        # is important because for finding starting point, we don't care about visited.
        for r, c in queue:
            size[r][c] = 1
        # run a bfs.
        while queue:
            r, c = queue.popleft()
            for nr, nc in self.neighbors(r, c, m, n):
                # always check whether a point has been visited or not
                if size[nr][nc] != 0:
                    continue
                if self._is_trough(nr, nc, m, n, size, matrix):
                    queue.append((nr, nc))
                    for nnr, nnc in self.neighbors(nr, nc, m, n):
                        size[nr][nc] = max(size[nr][nc], size[nnr][nnc] + 1)
                    result = max(result, size[nr][nc])
        return result

    def _is_trough(self, r, c, m, n, size, matrix):
        for nr, nc in self.neighbors(r, c, m, n):
            if size[nr][nc] != 0:
                continue
            if matrix[nr][nc] < matrix[r][c]:
                return False
        return True

    # I think this is even better then the direction.
    def neighbors(self, r, c, m, n):
        result = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + dr
            nc = c + dc
            if nr >= m or nr < 0 or nc >= n or nc < 0:
                continue
            result.append((nr, nc))
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.longestContinuousIncreasingSubsequence2([[1,2,3,4,5],
                                                     [16,17,24,23,6],
                                                     [15,18,25,22,7],
                                                     [14,19,20,21,8],
                                                     [13,12,11,10,9]])
    print(res)