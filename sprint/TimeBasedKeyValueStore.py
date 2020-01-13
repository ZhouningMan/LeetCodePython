from collections import defaultdict
import bisect

class TimeMapCustom:
    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key, val, ts):
        self.cache[key].append((val, ts))

    def get(self, key, ts):
        if key not in self.cache:
            return ""
        return self.binarySearch(key, ts)

    def binarySearch(self, key, ts):
        elements = self.cache[key]
        lo = 0
        hi = len(elements) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            element = elements[mid]
            if element[1] == ts:
                return element[0]
            elif element[1] > ts:
                hi = mid - 1
            else:
                lo = mid + 1
        return elements[hi][0] if hi >= 0 else ""

class TimeMap:
    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key, val, ts):
        self.cache[key].append((ts, val))

    def get(self, key, ts):
        if key not in self.cache:
            return ""
        elements = self.cache[key]
        # we don't want to compare the second dimension so put the biggest value there
        index = bisect.bisect(elements, (ts, chr(127)))
        if index >= 1:
            return elements[index-1][1]
        else:
            return ""
if __name__ == '__main__':
    tm = TimeMap()
# ["TimeMap","set","set","get","get","get","get","get"]
# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
    tm.set("love","high",10)
    tm.set("love","low",20)
    tm.get("love",5)
    tm.get("love",10)
    tm.get("love",15)
    tm.get("love",20)
    tm.get("love",25)

