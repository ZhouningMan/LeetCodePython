class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        if not nums or len(nums) == 1:
            return nums
        size = len(nums)
        i = size - 1
        while i > 0:
            # comparing neighboring values, only stop when
            # nums[i - 1] < nums[i]
            # this means nums[i: ] are in descending order
            if nums[i - 1] >= nums[i]:
                i -= 1
                continue
            j = self.ceiling(nums, nums[i-1], i)
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            self.reverse(nums, i, size - 1)
            return nums
        self.reverse(nums, 0, size - 1)
        return nums

    def ceiling(self, nums, val, start):
        j = start
        # find ceiling in a sorted list
        for i in range(start, len(nums)):
            if val >= nums[i]:
                return j
            j = i
        return j

    def reverse(self, nums, start, end):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

if __name__ == '__main__':
    s = Solution()
    ans = s.nextPermutation([1, 2])
    print(ans)