from collections import defaultdict
from collections import deque
import heapq


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        freq_map = defaultdict(int)
        for c in s:
            freq_map[c] += 1
        # max pq
        # (index, -frequency, count)
        # -frequency for sorting by max
        order_by_freq = [(f, c) for c, f in freq_map.items()]
        order_by_freq.sort(reverse=True)
        # first assigned a index for each character ordered by their frequency
        # if two character has the same index, the one with higher frequency wins.
        # The key is not to assigned (0, -freq, char) for all characters otherwise
        # this wil fails : aaabc, 2
        pq = [(i, -freq, char) for i, (freq, char) in enumerate(order_by_freq)]
        heapq.heapify(pq)
        j = 0
        sb = []
        while pq:
            i, freq, c = heapq.heappop(pq)
            if i > j:
                return ""
            sb.append(c)
            freq += 1
            j += 1
            if freq == 0:
                continue
            heapq.heappush(pq, (i + k, freq, c))
        return "".join(sb)
