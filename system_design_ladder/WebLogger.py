import collections

class WebLogger:

    def __init__(self):
        self.records = collections.deque()
    """
    @param: timestamp: An integer
    @return: nothing
    """

    def hit(self, timestamp):
        self.records.append(timestamp)
        self._remove_expired(timestamp)

    def _remove_expired(self, timestamp):
        while len(self.records) > 0 and self.records[0] <= timestamp - 300:
            self.records.popleft()
    """
    @param: timestamp: An integer
    @return: An integer
    """

    def get_hit_count_in_last_5_minutes(self, timestamp):
        self._remove_expired(timestamp)
        return len(self.records)
