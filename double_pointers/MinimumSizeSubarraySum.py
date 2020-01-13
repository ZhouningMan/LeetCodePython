class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """

    def minimumSize(self, nums, s):
        if nums is None or len(nums) == 0:
            return -1
        size = len(nums) + 1  # don't initialize to MAX_INT, just initialize to a bad value
        j = 0
        sum = 0  # contains [i, j) value
        for i in range(len(nums)):
            while sum < s and j < len(nums):
                sum += nums[j]  # when we increment secondary pointer, we always add to sum
                j += 1
            if sum >= s: # we have multiple conditions to exit, check the condition that is good for us
                size = min(size, j - i)
            sum -= nums[i]  # when we increment primary pointer, we subtract from the sum to invalidate the condition
        if size == len(nums) + 1:  # special condition deserves special treatment
            return -1
        return size