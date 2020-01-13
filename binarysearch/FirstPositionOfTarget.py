class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                end = mid  # this is the key
            else:
                end = mid - 1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def binarySearchFirstPosition(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] >= target:
                end = mid - 1
        if end + 1 < len(nums) and nums[end + 1] == target:
            return end + 1
        else:
            return -1

    def binarySearchLastPosition(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        if start - 1 >= 0 and nums[start - 1] == target:
            return start - 1
        else:
            return -1