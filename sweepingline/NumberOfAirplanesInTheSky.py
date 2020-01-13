"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from enum import Enum


class Event(Enum):
    land = 0
    takeoff = 1

    # define __lt__ for comparison
    def __lt__(self, other):
        return self.value < other.value


class Solution:

    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        if not airplanes or len(airplanes) == 0:
            return 0

        events = []
        # construct a list of events
        for schedule in airplanes:
            events.append((schedule.start, Event.takeoff))
            events.append((schedule.end, Event.land))
        # sort the events
        events.sort()
        count = 0
        max_count = 0
        # take action on each event
        for e in events:
            if e[1] == Event.takeoff:
                count += 1
            else:
                count -= 1
            max_count = max(count, max_count)
        return max_count

