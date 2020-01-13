
import heapq

class Pair:
    def __init__(self, nums, index):
        self.nums = nums
        self.index = index

    def __lt__(self, other):
        return self.nums[self.index] < other.nums[other.index]

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        if not arrays:
            return None
        pq = []
        for arr in arrays:
            if not arr:
                continue
            heapq.heappush(pq, Pair(arr, 0))
        ans = []
        while pq:
            pair = heapq.heappop(pq)
            ans.append(pair.nums[pair.index])
            if pair.index < len(pair.nums) - 1:
                heapq.heappush(pq, Pair(pair.nums, pair.index + 1))
        return ans
