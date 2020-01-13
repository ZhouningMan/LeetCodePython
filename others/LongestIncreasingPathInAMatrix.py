class Solution:
    DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def longestIncreasingPath(self, matrix) -> int:
        if matrix is None or len(matrix) == 0:
            return 0
        longest = 0
        rows = len(matrix)
        cols = len(matrix[0])
        # this memory matrix can also acts as visited matrix, we don't need a separate one for it.
        cache = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, self.dfs(matrix, cache, r, c))
        return longest

    def dfs(self, matrix, cache, r, c):
        length = 1
        for dr, dc in Solution.DIRECTIONS:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] > matrix[r][c]:
                child_path = cache[nr][nc]
                if child_path == 0:
                    child_path = self.dfs(matrix, cache, nr, nc)
                length = max(length, child_path + 1)
        cache[r][c] = length  # cache the result
        return length

    @staticmethod
    def print(memory):
        for row in memory:
            print(row)


if __name__ == '__main__':
    Solution().longestIncreasingPath([[7,6,1,1],[2,7,6,0],[1,3,5,1],[6,6,3,2]])