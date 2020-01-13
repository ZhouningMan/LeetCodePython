class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        if not nums:
            return 0
        size = len(nums)
        left, right = 0, size - 1
        count = 0
        nums.sort()  # don't forget to sort this
        while left < right:
            s = nums[left] + nums[right]
            if s > target:
                count += right - left
                right -= 1
            else:
                left += 1  # increment the left
        return count
