from collections import defaultdict
import heapq

class Solution:
    def impl(self, s):
        char_count = defaultdict(int)
        # count of each characters
        for c in s:
            char_count[c] += 1
        freq_count = defaultdict(int)
        # count of each frequency
        for freq in char_count.values():
            freq_count[freq] += 1
        max_heap = [(-freq, count) for freq, count in freq_count.items()]
        max_heap.append((0, 0))
        heapq.heapify(max_heap)
        deletes = 0
        # drop one character at a time
        while len(max_heap) > 1:
            f1, c1 = heapq.heappop(max_heap)
            f2, c2 = heapq.heappop(max_heap)
            delta = c1 - 1
            f1 += 1
            deletes += delta
            if f1 == f2 and c2 + delta > 1:
                heapq.heappush(max_heap, (f2, c2 + delta))
            else:
                if delta > 1:
                    heapq.heappush(max_heap, (f1, delta))
                heapq.heappush(max_heap, (f2, c2))
        return deletes

if __name__ == '__main__':
    s = Solution()
    ans = s.impl("example")
    print(ans)

