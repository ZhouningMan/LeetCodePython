class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        m = len(nums)
        dp = [1] * m
        parent = [-1] * m
        nums.sort()
        dp[0] = 1
        for i in range(1, m):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
        idx = 0
        max_size = 0
        for i, v in enumerate(dp):
            if v > max_size:
                max_size = v
                idx = i
        largest = set()
        while idx != -1:
            largest.add(nums[idx])
            idx = parent[idx]
        return list(largest)
