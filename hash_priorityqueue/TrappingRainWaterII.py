import heapq


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        if not heights or len(heights) == 0:
            raise ValueError("...")

        min_q = []
        m = len(heights)
        n = len(heights[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        # first initialize th circle to form a water bucket
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    heapq.heappush(min_q, (heights[r][c], r, c))
                    visited[r][c] = True
        water = 0
        # continuously tighten the encirclement, basically for every iteration
        # we have a valid encirclement
        while len(min_q) > 0:
            height, r, c = heapq.heappop(min_q)
            for d in DIRECTIONS:
                next_r = d[0] + r
                next_c = d[1] + c
                if 0 <= next_r < m and 0 <= next_c < n and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    next_h = heights[next_r][next_c]
                    water += max(0, height - next_h)
                    # this is the hardest step, but once you understand, it makes a lot of
                    # sense, basically you tighten the encirclement at position
                    # (next_r, next_c) either with higher piece of wood. but you always
                    # move inward.
                    heapq.heappush(min_q, (max(next_h, height), next_r, next_c))
        return water

if __name__ == '__main__':
    s = Solution()
    print(s.trapRainWater([[1,2,1],
                           [2,0,2],
                           [1,2,1]]))
