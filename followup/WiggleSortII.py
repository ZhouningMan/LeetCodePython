class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        if not nums:
            return
        m = len(nums)
        self.find_median(nums)
        copy = [0] * m
        even = 0
        odd = 1
        median_idx = (m - 1)//2
        for i in reversed(range(0, median_idx + 1)):
            copy[even] = nums[i]
            even += 2
        for i in reversed(range(median_idx + 1, m)):
            copy[odd] = nums[i]
            odd += 2
        for i, val in enumerate(copy):
            nums[i] = val

    def find_median(self, nums):
        start = 0
        end = len(nums) - 1
        target = len(nums) // 2
        while start <= end:
            j = self.partition(nums, start, end)
            if j == target:
                return nums[j]
            elif j < target:
                start = j + 1
            else:
                end = j - 1
        return nums[end]

    def partition(self, nums, start, end):
        if start >= end:
            return start
        pivot = nums[start]
        i = start + 1
        j = end
        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        nums[start], nums[j] = nums[j], nums[start]
        return j

if __name__ == '__main__':
    s = Solution()
    for nums in [ [1, 3, 2, 2, 3, 1], [1, 4, 1, 5, 1, 6,7], [4,5,5,6]]:
        s.wiggleSort(nums)
        print(nums)
