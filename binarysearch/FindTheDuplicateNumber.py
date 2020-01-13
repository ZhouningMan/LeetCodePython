class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):

        start = 1
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            count = self._le(nums, mid)
            if count > mid:
                end = mid - 1
            else:
                start = mid + 1
        # once the loop exit, start - end = 1
        return start

    def _le(self, nums, mid):
        count = 0
        for num in nums:
            if num <= mid:
                count += 1
        return count