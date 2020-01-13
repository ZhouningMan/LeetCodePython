class Memcache:
    INVALID = 2147483647

    def __init__(self):
        self.cache = {}

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    def get(self, curtTime, key):
        if key not in self.cache.keys():
            return Memcache.INVALID
        val, ts, ttl = self.cache.get(key)
        if ttl == 0 or ts + ttl - 1 >= curtTime:
            return val
        self.delete(curtTime, key)
        return Memcache.INVALID

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    def set(self, curtTime, key, value, ttl):
        self.cache[key] = (value, curtTime, ttl)

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    def delete(self, curtTime, key):
        if key in self.cache.keys():
            del self.cache[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def incr(self, curtTime, key, delta):
        # increment or decrement doesn't reset the time stamp, which is a werid requirement
        if key not in self.cache.keys() or self.get(curtTime, key) == Memcache.INVALID:
            return Memcache.INVALID
        val, ts, ttl = self.cache.get(key)
        val += delta
        self.set(ts, key, val, ttl)
        return val

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def decr(self, curtTime, key, delta):
        return self.incr(curtTime, key, -delta)


if __name__ == '__main__':
    cache = Memcache()
    print(cache.get(1, 0))
    print(cache.set(2, 1, 1, 2))
    print(cache.get(3, 1))
    print(cache.get(4, 1))