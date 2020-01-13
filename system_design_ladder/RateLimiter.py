import collections
import bisect

class HitHistory:
    def __init__(self, count, period, hits):
        self.count = count
        self.period = period
        self.hits = hits

    def hit_limit(self, timestamp):
        i = bisect.bisect_left(self.hits, timestamp - self.period) # equal values on the right
        return len(self.hits) - i >= self.count

    # def remove_expired_hits(self, timestamp):
    #     while len(self.hits) > 0 and timestamp - self.hits[0] >= self.period:
    #         self.hits.popleft()

    def hit(self, timestamp):
        self.count += 1
        self.hits.append(timestamp)

    def update(self, count, period):
        self.count = count
        self.period = period


class Solution:
    TIME_UNIT_MAP = {"s": 1,
                     "m": 60,
                     "h": 3600,
                     "d": 3600 * 24}

    def __init__(self):
        self.event_rate = {}

    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: true or false to indicate the event is limited or not
    """
    def isRatelimited(self, timestamp, event, rate, increment):
        count, period = self._convert_rate(rate)
        hit_history = self.event_rate.get(event, HitHistory(count, period, []))
        hit_history.update(count, period)
        # hit_history.remove_expired_hits(timestamp)
        self.event_rate[event] = hit_history
        if hit_history.hit_limit(timestamp):
            return True
        if increment:
            hit_history.hit(timestamp)
        return False

    def _convert_rate(self, rate):
        vals = rate.split("/")
        period = Solution.TIME_UNIT_MAP[vals[1]]
        return int(vals[0]), period


if __name__ == '__main__':
    solution = Solution()
    print(solution.isRatelimited(1, "login", "1/s", True))
    print(solution.isRatelimited(61, "login", "1/m", True))