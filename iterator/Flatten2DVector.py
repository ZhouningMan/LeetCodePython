class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        if not vec2d:
            self.outer = [[], 0]
            self.inner = [[], 0]
        else:
            self.outer = [vec2d, 1]
            self.inner = [vec2d[0], 0]

    # @return {int} a next element
    def next(self):
        inner = self.inner
        val = inner[0][inner[1]]
        inner[1] += 1
        return val

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        outer = self.outer
        while self._hasNext(outer):
            if self._hasNext(self.inner):
                return True
            self.inner = [outer[0][outer[1]], 0]
            outer[1] += 1
        return self._hasNext(self.inner)

    def _hasNext(self, pair):
        if pair[1] == len(pair[0]):
            return False
        else:
            return True


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

if __name__ == '__main__':
    i, v  = Vector2D([[1,2],[3],[4,5,6]]), []
    while i.hasNext():
        print(v)
        v.append(i.next())
