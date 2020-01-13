class Solution:
    def spiralMatrixIII(self, R: int, C: int, r: int, c: int):
        result = []
        left = c
        right = left + 1
        top = r
        bottom = r + 1
        while len(result) < R * C:
            for i in range(left, right + 1):
                self.add_if_valid(result, R, C, top, i)
            left -= 1
            for i in range(top + 1, bottom + 1):
                self.add_if_valid(result, R, C, i, right)
            for i in range(right - 1, left - 1, -1):
                self.add_if_valid(result, R, C, bottom, i)
            right += 1
            top -= 1
            for i in range(bottom - 1, top, -1):
                self.add_if_valid(result, R, C, i, left)
            bottom += 1
        return result

    def add_if_valid(self, result, R, C, r, c):
        if 0 <= r < R and 0 <= c < C:
            result.append([r, c])


if __name__ == '__main__':
    s = Solution()
    ans = s.spiralMatrixIII(5, 6, 1, 4)
    print(ans)