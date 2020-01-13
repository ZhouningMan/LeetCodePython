class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            elif nums[mid] == nums[end]:
                end -= 1
            else:
                end = mid
        return min(nums[start], nums[end])

