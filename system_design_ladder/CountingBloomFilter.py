class HashFunction:
    def __init__(self, mul, offset, limit):
        self.mul = mul
        self.offset = offset
        self.limit = limit

    def hash_code(self, word):
        ans = self.offset
        for c in word:
            ans = (ans * self.mul + ord(c)) % self.limit
        return ans

class CountingBloomFilter:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.bit_set = [0] * 10000
        self.hash_funcs = []
        for i in range(k):
            self.hash_funcs.append(HashFunction(i * 3 + 7, i * 11 + 33, 10000))
    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        for f in self.hash_funcs:
            self.bit_set[f.hash_code(word)] += 1

    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        for f in self.hash_funcs:
            if self.bit_set[f.hash_code(word)] <= 0:
                return False
        return True

    def remove(self, word):
        for f in self.hash_funcs:
            self.bit_set[f.hash_code(word)] -= 1
