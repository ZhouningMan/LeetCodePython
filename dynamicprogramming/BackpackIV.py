class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        n = len(nums)
        dp = [0] * (target + 1)
        for i in range(n + 1):
            for j in range(target + 1):
                if j == 0 and i == 0:
                    dp[j] = 1
                elif j == 0:
                    dp[j] = 1
                elif i == 0:
                    dp[i] = 0
                elif j - nums[i-1] >= 0:
                    # transition function:
                    # dp[i][j] = dp[i-1][j] + dp[i][j- nums[i-1]]
                    # each number can be used unlimited times
                    dp[j] = dp[j] + dp[j - nums[i-1]]
        return dp[target]


    def backPackIVDFS(self, nums, target):
        return self.dfs(nums, len(nums) - 1, target, {})

    def dfs(self, nums, i, target, memo):
        if (i, target) in memo:
            return memo[(i, target)]
        if i < 0:
            return 0
        if target == 0:
            return 1
        count = 0
        count += self.dfs(nums, i-1, target, memo)
        if target - nums[i] >= 0:
            count += self.dfs(nums, i, target - nums[i], memo)
        memo[(i, target)] = count
        return count





if __name__ == '__main__':
    s = Solution()
    print(s.backPackIV([1, 2], 2))
