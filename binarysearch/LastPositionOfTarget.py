class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                start = mid  # this is the key
            else:
                end = mid - 1
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1