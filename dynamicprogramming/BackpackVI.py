class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackVIDFS(self, nums, target):
        return self.dfs(nums, target, {})

    def backPackVI(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]


    def dfs(self, nums, target, memo):
        if target in memo:
            return memo[target]
        if target == 0:
            return 1
        if target < 0:
            return 0
        count = 0
        for num in nums:
            count += self.dfs(nums, target - num, memo)
        memo[target] = count
        return count