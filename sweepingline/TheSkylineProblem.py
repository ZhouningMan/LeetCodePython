from enum import Enum
import heapq


class Event(Enum):
    enter = 0
    exit = 1

    def __lt__(self, other):
        return self.value - other.value

class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def buildingOutline(self, buildings):
        if not buildings or len(buildings) == 0:
            return []
        events = []
        for i, b in enumerate(buildings):
            events.append((b[0], Event.enter, b[2]))
            events.append((b[1], Event.exit, b[2]))
        events.sort()

        max_q = [0]
        points = []
        for (x, event, height) in events: # for each events
            if event == Event.enter:
                heapq.heappush(max_q, -height)
            else:
                # o(n) removal
                max_q.remove(-height)
                heapq.heapify(max_q)
            max_height = -max_q[0]
            # deal with special case, don't mix it with other cases
            if len(points) == 0:
                points.append([x, max_height])
                continue

            if points[-1][0] == x: # use the higher values
                points[-1][1] = max(max_height, points[-1][1])
            # no height change, we don't need to duplicate the result
            elif points[-1][1] != max_height:
                points.append([x, max_height])

        return self.merge(points)

    def merge(self, points):
        result = []
        last_seg = [points[0][0], 0, points[0][1]]
        for i in range(1, len(points)):
            last_seg[1] = points[i][0]
            if last_seg[2] > 0: # if height == 0, we don't need it
                result += [last_seg]
            last_seg = [points[i][0], 0, points[i][1]]
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.buildingOutline([[1,3,3],[2,4,4],[5,6,1]])
    print(res)