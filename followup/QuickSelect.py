class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        if not nums or n > len(nums):
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            j = self.partition(nums, start, end)
            if j + 1 == n:
                return nums[j]
            elif j + 1 < n:
                start = j + 1
            else:
                end = j - 1
        return end

    def partition(self, nums, start, end):
        pivot = nums[start]
        i = start + 1
        j = end
        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1
            while i <= j and nums[j] < pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        nums[start], nums[j] = nums[j], nums[start]
        return j
