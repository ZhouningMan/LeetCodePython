"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        if not points:
            return []
        top_k = []
        for p in points:
            dist = (p.x - origin.x) ** 2 + (p.y - origin.y) ** 2
            # python use min pq, if we want to order by max, we need to negate the value. 
            heapq.heappush(top_k, (-dist, -p.x, -p.y))  # reverse the sorting order
            if len(top_k) > k:
                heapq.heappop(top_k)
        ans = []
        while top_k:
            element = heapq.heappop(top_k)
            ans.append(Point(-element[1], -element[2]))
        # reverse the order to get the value from smallest to largest
        ans.reverse()
        return ans
