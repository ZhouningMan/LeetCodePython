import sys
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        if not triangle or len(triangle) == 0:
            return 0
        rows = len(triangle)
        # using 1D array since the result only depends on previous row and column
        sum = [sys.maxsize] * rows
        for r in range(rows):
            # this is the key. We need to reverse the iteration, otherwise, it won't work
            for c in range(r, -1, -1):
                val = triangle[r][c]
                if c == 0 and r == 0:
                    sum[c] = val
                elif c == 0:
                    sum[c] = sum[c] + val
                elif c == r:
                    sum[c] = sum[c-1] + val
                else:
                    sum[c] = min(sum[c-1], sum[c]) + val
            print(sum)
        return min(sum)

