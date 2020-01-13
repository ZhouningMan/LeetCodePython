from collections import defaultdict
import heapq

class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        freq_map = defaultdict(int)
        for v in nums:
            freq_map[v] += 1
        top_k = []
        # nlogk
        for num, freq in freq_map.items():
            heapq.heappush(top_k, (freq, num))
            if len(top_k) > k:
                heapq.heappop(top_k)
        ans = []
        # klogk
        while top_k:
            ans.append(heapq.heappop(top_k)[1])
        ans.reverse()
        return ans