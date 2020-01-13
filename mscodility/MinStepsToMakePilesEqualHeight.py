class Solution:
    def impl(self, nums):
        nums.sort()
        steps = 0
        total = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                steps += 1
            total += steps
        return total

if __name__ == '__main__':
    s = Solution()
    print(s.impl([5, 2, 2, 3, 1, 1]))