import heapq

class Item:
    def __init__(self, li, idx):
        self.li = li
        self.idx = idx
    # reverse comparator
    def __lt__(self, other):
        return other.li[other.idx] < self.li[self.idx]

    def end(self):
        return len(self.li) == self.idx + 1

class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        for arr in arrays:
            arr.sort(reverse=True)
        maxQ = []
        for arr in arrays:
            if arr:
                heapq.heappush(maxQ, Item(arr, 0))
        for _ in range(k):
            item = heapq.heappop(maxQ)
            if not item.end():
                heapq.heappush(maxQ, Item(item.li, item.idx + 1))
        return item.li[item.idx]