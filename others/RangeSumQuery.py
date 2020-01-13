class NumArray:

    def __init__(self, nums):
        # initialize to zero, let the update populate the value
        self.nums = [0] * len(nums)
        # BIT is one-based
        self.bit = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):
            self.update(i, v)

    def update(self, i, val):
        # delta is calculated by val - self.nums[i] not vice versa
        delta = val - self.nums[i]
        self.nums[i] = val
        # BIT is one-based
        i += 1
        while i < len(self.bit):
            self.bit[i] += delta
            i += self.lowbit(i)

    def sumRange(self, i, j):
        # application of prefix sum to calculate the range value
        return self.sum(j) - self.sum(i - 1)

    def sum(self, i):
        ans = 0
        # need to increment the index
        i += 1
        while i > 0:
            ans += self.bit[i]
            i -= self.lowbit(i)
        return ans

    def lowbit(self, i):
        return i & (-i)

if __name__ == '__main__':
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    s = NumArray(input)
    print(s.bit)