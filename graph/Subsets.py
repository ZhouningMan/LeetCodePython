class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        if not nums:
            return [[]]
        ans = []
        subset = []
        nums.sort()
        self.dfs(nums, 0, ans, subset)
        return ans

    def dfs(self, nums, idx, ans, subset):
        if idx == len(nums):
            ans.append(list(subset))
            return
        # explicitly not picking the solution
        self.dfs(nums, idx + 1, ans, subset)  # not include this number
        subset.append(nums[idx])
        self.dfs(nums, idx + 1, ans, subset)
        subset.pop()  # pop last element
