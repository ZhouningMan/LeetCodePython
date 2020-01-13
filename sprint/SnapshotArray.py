from collections import defaultdict
import bisect

class SnapVal:
    def __init__(self, snapId, val):
        self.snapId = snapId
        self.val = val

    def __lt__(self, other):
        return self.snapId < other.snapId

class SnapshotArray:
    def __init__(self, length):
        self.dict = defaultdict(list)
        self.snapId = 0

    def set(self, index, val):
        snaps = self.dict[index]
        size = len(snaps)
        if size == 0:
            snaps.append(SnapVal(self.snapId, val))
        elif snaps[size - 1].snapId == self.snapId:
            snaps[size - 1].val = val
        else:
            snaps.append(SnapVal(self.snapId, val))

    def snap(self):
        old = self.snapId
        self.snapId += 1
        return old

    def get(self, index, snapId):
        snaps = self.dict[index]
        pos = bisect.bisect_right(snaps, SnapVal(snapId, 0))
        if pos == 0:
            return 0
        lastSnap = snaps[pos - 1]
        if snaps[-1].snapId < lastSnap.snapId:
            return None
        else:
            return lastSnap.val

if __name__ == '__main__':
    s = SnapshotArray(3)
    s.set(0, 5)
    s.snap()
    s.set(0, 6)
    print(s.get(0, 0))