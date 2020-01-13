class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        if not nums:
            return []
        win_sum = []
        s = 0
        for i, val in enumerate(nums):
            s += val
            if i >= k:
                s -= nums[i - k]
                win_sum.append(s)
            elif i == k - 1:
                win_sum.append(s)
        return win_sum