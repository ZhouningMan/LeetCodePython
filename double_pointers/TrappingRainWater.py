import heapq


class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        if not heights or len(heights) <= 2:
            return 0
        min_q = []
        heapq.heappush(min_q, (heights[0], 0))
        heapq.heappush(min_q, (heights[-1], len(heights) - 1))
        water = 0
        # identical idea to trapper water 2. Build the bucket from outer wood
        # and keep moving in, if we find a better wood(whose value is greater than the existing wood)
        # we use that piece of wood, otherwise keep the old piece
        while True:
            # this is log(2) which is constant
            val, min_idx = heapq.heappop(min_q)
            # heapq is only used to ease our implementation, it at most contains 2 elements
            if abs(min_idx - min_q[0][1]) == 1:
                break
            next_idx = min_idx + 1 if min_idx < min_q[0][1] else min_idx - 1
            water += max(0, val - heights[next_idx])
            if heights[next_idx] > val:
                heapq.heappush(min_q, (heights[next_idx], next_idx))
            else:
                heapq.heappush(min_q, (val, next_idx))
        return water
