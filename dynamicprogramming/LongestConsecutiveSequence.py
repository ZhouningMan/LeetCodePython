class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, nums):
        if not nums:
            return 0
        ans = 0
        nums_set = set(nums)
        for v in nums:
            if v not in nums_set:
                continue
            left = v
            right = v + 1
            while left in nums_set:
                nums_set.remove(left)
                left -= 1
            while right in nums_set:
                nums_set.remove(right)
                right += 1
            ans = max(ans, right - left - 1)
        return ans

