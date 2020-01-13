class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        if nums is None:
            return []
        ans = []
        self.dfs(nums, [], ans)
        return ans

    def dfs(self, nums, chosen, ans):
        if not nums:
            ans.append(list(chosen))
            return
        size = len(nums)
        for i in range(size):
            chosen.append(nums[i])
            self.dfs(nums[0:i] + nums[i+1:], chosen, ans)
            chosen.pop()
