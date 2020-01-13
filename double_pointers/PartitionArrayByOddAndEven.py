class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        if not nums:
            return
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
