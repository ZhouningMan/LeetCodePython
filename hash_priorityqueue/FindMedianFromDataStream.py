import heapq


class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def __init__(self):
        self.max_q = []
        self.min_q = []

    def medianII(self, nums):
        result = []
        for num in nums:
            self.add_num(num)
            result += [self.get_median()]
        return result

    def add_num(self, num):
        # always add to max queue
        heapq.heappush(self.max_q, -num)
        # re-balance, move the top of max queue to min queue
        if len(self.max_q) > len(self.min_q):
            heapq.heappush(self.min_q, -heapq.heappop(self.max_q))
        # swap the extreme value of max_q and min_q if they are out of place
        elif -self.max_q[0] > self.min_q[0]:
            first, second = -heapq.heappop(self.max_q), heapq.heappop(self.min_q)
            heapq.heappush(self.min_q, first)
            heapq.heappush(self.max_q, -second)

    def get_median(self):
        if len(self.min_q) > len(self.max_q):
            return self.min_q[0]
        else:
            return -self.max_q[0]

if __name__ == '__main__':
    s = Solution()
    print(s.medianII([1,2,3,4,5]))