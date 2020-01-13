class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        nuLm.sort()
        ans = []
        self.dfs(num, target, [], 0, 0, ans)
        return ans

    def dfs(self, num, target, chosen, index, curr_sum, answer):
        if curr_sum == target:
            answer.append(list(chosen))
            return
        if index == len(num):  # no answer found
            return
        for i in range(index, len(num)):
            if num[i] + curr_sum > target:  # no more better candidates
                break
                # deduplicate
            if i > index and num[i] == num[i - 1]:
                continue
            chosen.append(num[i])
            # increment the index
            self.dfs(num, target, chosen, i + 1, curr_sum + num[i], answer)
            chosen.pop()

