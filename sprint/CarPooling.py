from collections import namedtuple

Event = namedtuple("Event", ["people", "loc", "action"])
START = 1
END = 0

class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        events = []
        for trip in trips:
            people = trip[0]
            start = trip[1]
            end = trip[2]
            events.append(Event(people, start, START))
            events.append(Event(people, end, END))
        events.sort(key=lambda e: (e.loc, e.action))

        total = 0
        for e in events:
            if e.action == START:
                total += e.people
            else:
                total -= e.people
            if total > capacity:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    s.carPooling([[2,1,5],[3,3,7]], 4)