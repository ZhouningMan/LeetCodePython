class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        if not nums:
            return 0
        sequence = nums[0]
        ans = sequence
        for i in range(1, len(nums)):
            num = nums[i]
            # find the longest contiguous sequence END at nums[i]
            sequence = max(num + sequence, num)
            ans = max(sequence, ans)
        return ans