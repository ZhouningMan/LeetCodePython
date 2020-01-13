class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if not nums:
            return 0
        # we have to sort, so a pattern could emerge
        nums.sort()
        le, ri = 0, len(nums) - 1
        count = 0
        while le < ri:
            # de-deup
            if le > 0 and nums[le] == nums[le - 1]:
                le += 1
                continue
            # de-deup
            if ri < len(nums) - 1 and nums[ri] == nums[ri + 1]:
                ri -= 1
                continue
            sum = nums[le] + nums[ri]
            if sum == target:
                count += 1
                le += 1
                ri -= 1
            elif sum > target:
                ri -= 1
            else:
                le += 1
        return count
