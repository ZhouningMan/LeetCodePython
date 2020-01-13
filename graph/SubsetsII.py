class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        if nums is None:
            return []
        nums.sort()
        ans = []
        self.dfs(nums, [], 0, ans)
        return ans

    def dfs(self, nums, chosen, index, answer):
        answer.append(list(chosen)) # not picking the current value
        print(f"chosen={chosen}, index={index}")
        if index == len(nums):
            return
        # chosen is the prefix, add the prefix to sebsets of nums[index:]
        for i in range(index, len(nums)):
            # deduplicating
            if i > index and nums[i] == nums[i - 1]:
                continue
            chosen.append(nums[i])
            self.dfs(nums, chosen, i + 1, answer)
            chosen.pop()

if __name__ == '__main__':
    s = Solution()
    s.subsetsWithDup([1,2])