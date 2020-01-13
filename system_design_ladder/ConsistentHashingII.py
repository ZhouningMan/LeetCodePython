import random


class Solution:

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.min = self.n
        self.code_to_machine = {}

    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """
    @classmethod
    def create(cls, n, k):
        return cls(n, k)

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """
    def addMachine(self, machine_id):
        count = 0
        ids = []
        while count < self.k:
            j = random.randrange(self.n)
            if j in self.code_to_machine:
                continue
            self.code_to_machine[j] = machine_id
            self.min = min(self.min, j)
            ids.append(j)
            count += 1
        return ids


    """
    @param: hashcode: An integer
    @return: A machine id
    """
    def getMachineIdByHashCode(self, hashcode):
        target = hashcode % self.n
        code = self.n
        for key, val in self.code_to_machine.items():
            if key == target:
                return val
            if key > target:
                code = min(code, key)
        if code in self.code_to_machine:
            return self.code_to_machine[code]
        else:
            return self.code_to_machine[self.min]


if __name__ == '__main__':
    solution = Solution.create(100, 3)
    print(solution.addMachine(1))
    print(solution.getMachineIdByHashCode(4))
    print(solution.addMachine(2))
    print(solution.getMachineIdByHashCode(61))
    print(solution.getMachineIdByHashCode(91))
