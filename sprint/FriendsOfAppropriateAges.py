import bisect
import math
from collections import Counter


class Solution:
    def numFriendRequests1(self, ages: List[int]) -> int:
        ages.sort()
        total = 0
        for i, v in enumerate(ages):
            lower = 0.5 * v + 7
            left = bisect.bisect_right(ages, lower)
            right = bisect.bisect_right(ages, v)
            total += max(right - left - 1, 0)
        return total

    def numFriendRequests(self, ages):
        def request(a, b):
            return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)

        counter = Counter(ages)
        total = 0
        for a in counter:
            for b in counter:
                if not request(a, b):
                    continue
                ca = counter[a]
                cb = counter[b]
                # cannot make friend with oneself
                if a == b:
                    cb -= 1
                total += ca * cb
        return total

    # wrong implementation
    def numFriendRequests2(self, ages):
        count = [0] * 121
        for i in ages:
            count[i] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        total = 0
        print(count)
        for i, c in enumerate(count):
            lower = math.ceil(0.5 * i + 7)
            candidates = c - 1
            if lower > 0:
                candidates -= count[lower - 1]
            # every body with age i can make friends with candidates
            # there are c person with age i
            total += c * candidates
        return total