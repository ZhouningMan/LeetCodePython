class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid
        return max(nums[start], nums[end])


    def mountainSequence2(self, nums):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_top(nums, mid):
                return mid
            elif (mid > 0 and nums[mid-1] < nums[mid]) or nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
        return end if nums[end] > nums[start] else start

    def is_top(self, nums, mid):
        if len(nums) == 1:
            return True
        if mid == 0:
            return nums[0] > nums[1]
        if mid == len(nums) - 1:
            return nums[mid] > nums[mid - 1]
        return nums[mid-1] < nums[mid] > nums[mid+1]

    def mountainSequence3(self, nums):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if mid == len(nums) - 1:
                return nums[mid]
            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1
        return nums[end] if nums[end] > nums[start] else nums[start]