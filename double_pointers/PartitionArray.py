class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        if not nums:
            return 0
        i = 0
        end = len(nums) - 1
        while i <= end:
            if nums[i] >= k:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            else:
                i += 1
        return end + 1  # nums[end] is less than k
