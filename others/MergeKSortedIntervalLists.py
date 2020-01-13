"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class IndexedList:
    def __init__(self, index, list):
        self.index = index
        self.list = list

    def __lt__(self, other):
        return self.get_interval().start < other.get_interval().start

    def get_interval(self):
        return self.list[self.index]

    def end(self):
        return self.index == len(self.list) - 1

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        if not intervals:
            return []
        remaining = []
        for itv in intervals:
            if itv:
                heapq.heappush(remaining, IndexedList(0, itv))
        result = []
        while remaining:
            segment = heapq.heappop(remaining)
            self.add_to(result, segment.get_interval())
            if not segment.end():
                heapq.heappush(remaining, IndexedList(segment.index + 1, segment.list))
        return result

    def add_to(self, result, interval):
        if not result:
            result.append(interval)
            return
        last = result[-1]
        if last.end < interval.start:
            result.append(interval)
        else:
            last.end = max(interval.end, last.end)