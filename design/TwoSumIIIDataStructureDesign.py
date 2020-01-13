from collections import defaultdict

class TwoSum:

    def __init__(self):
        self.nums = defaultdict(int)

    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        self.nums[number] += 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        for v in self.nums:
            if value - v in self.nums:
                if value - v == v:
                    return self.nums[v] >= 2
                return True
        return False