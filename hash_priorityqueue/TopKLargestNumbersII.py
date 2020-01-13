import heapq

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.k = k
        self.queue = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        heapq.heappush(self.queue, num)
        if len(self.queue) > self.k:
            heapq.heappop(self.queue)

    """
    @return: Top k element
    """
    def topk(self):
        return sorted(self.queue, reverse=True)


# offline algorithm
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        heapq.heapify(nums)
        top_k = heapq.nlargest(k, nums)
        top_k.sort()
        top_k.reverse()
        return top_k
