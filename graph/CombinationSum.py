class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()
        ans = []
        self.dfs(candidates, target, 0, [], ans)
        return ans

    def dfs(self, candidates, target, i, chosen, ans):
        if target == 0:  # this is the first terminating condition
            ans.append(list(chosen))
            return
        if i == len(candidates):  # cannot find an answer
            return
        # pick ith number
        ith = candidates[i]
        if ith > target:  # optimize
            return

        if i > 0 and candidates[i-1] == ith:
            # don't pick current one
            self.dfs(candidates, target, i + 1, chosen, ans)
            return

        chosen.append(ith)
        self.dfs(candidates, target - ith, i, chosen, ans)
        chosen.pop()
        self.dfs(candidates, target, i + 1, chosen, ans)


if __name__ == '__main__':
    s = Solution()
    s.combinationSum([2,3,6,7], 7)