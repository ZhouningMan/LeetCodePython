class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        top_r = 0
        bot_r = n - 1
        left_c = 0
        right_c = n - 1

        i = 1
        while top_r <= bot_r and left_c <= right_c:
            for c in range(left_c, right_c + 1):
                matrix[top_r][c] = i
                i += 1
            for r in range(top_r + 1, bot_r + 1):
                matrix[r][right_c] = i
                i += 1
            if top_r == bot_r:
                break
            for c in reversed(range(left_c, right_c)):
                matrix[bot_r][c] = i
                i += 1
            for r in reversed(range(top_r + 1, bot_r)):
                matrix[r][left_c] = i
                i += 1
            top_r += 1
            bot_r -= 1
            left_c += 1
            right_c -= 1
        return matrix

