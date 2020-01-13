"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from enum import Enum

class Event(Enum):
    end = 0
    start = 1

    def __lt__(self, other):
        return self.value - other.value


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        if not intervals or len(intervals) == 0:
            return 0

        events = []
        for itv in intervals:
            events.append((itv.start, Event.start))
            events.append((itv.end, Event.end))
        events.sort()

        count = 0
        max_count = 0
        for e in events:
            if e[1] == Event.start:
                count += 1
            else:
                count -= 1
            max_count = max(count, max_count)

        return max_count
