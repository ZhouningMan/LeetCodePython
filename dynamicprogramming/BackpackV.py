class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        n = len(nums)
        dp = [0] * (target + 1)
        prefix_sum = 0
        dp[0] = 1
        for i in range(1, n + 1):
            prefix_sum += nums[i - 1]
            for j in reversed(range(min(target, prefix_sum) + 1)):
                if j - nums[i - 1] >= 0:
                    dp[j] = dp[j] + dp[j - nums[i - 1]]
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    s.backPackV([1,2,3,3,7], 7)