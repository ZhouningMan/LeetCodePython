class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        start = min(nums)
        end = max(nums)
        error = 0.00001
        while start + error < end:
            mid = (start + end) / 2
            if self._satisfy(nums, mid, k):
                # try a better solution
                start = mid
            else:
                end = mid
        return start

    def _satisfy(self, nums, average, k):
        # initialize prefix sum to zero
        right_sum = 0
        left_sum = 0
        # min sum is the sum between [0, i-k]
        min_sum = 0
        for i in range(len(nums)):
            right_sum += nums[i] - average
            if i >= k:
                left_sum += nums[i - k] - average
                min_sum = min(left_sum, min_sum)
            if i >= k - 1 and right_sum - min_sum >= 0:
                return True
        return False