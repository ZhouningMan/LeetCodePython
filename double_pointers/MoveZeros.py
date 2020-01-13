class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        if not nums:
            return

        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[i], nums[i-count] = nums[i-count], nums[i]
