"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


from enum import Enum

class Status(Enum):
    # logoff comes before login
    logoff = 0
    login = 1

    def __lt__(self, other):
        return self.value - other.value

class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """
    def timeIntersection(self, seqA, seqB):
        if not seqA or not seqB or len(seqA) == 0 or len(seqB) == 0:
            return []
        events = []
        # never allow duplicate code
        user_status = {'A': seqA, 'B': seqB}
        for user, seq in user_status.items():
            for itv in seq:
                events.append((itv.start, Status.login, user))
                events.append((itv.end, Status.logoff, user))

        events.sort()
        online = set()
        start = None
        result = []
        # sweeping line template
        for e in events:
            if e[1] == Status.login:
                online.add(e[2])
            else:
                online.remove(e[2])
            # find the interval where we have both users
            if len(online) == 2:
                if start is None:
                    # first time, two users are online
                    start = e[0]
            else:
                if start is not None:
                    # first time, two user are not online
                    result.append(Interval(start, e[0]))
                start = None
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.timeIntersection([Interval(1,2),Interval(5,100)], [Interval(1,6)]))
