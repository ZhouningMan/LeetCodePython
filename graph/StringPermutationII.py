class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        if not str:
            return [""]
        str = sorted(str)
        ans = []
        self.dfs(str, [], ans)
        return ans

    def dfs(self, str, chosen, ans):
        if not str:
            ans.append("".join(chosen))

        for i, ch in enumerate(str):
            # deduplicate
            if i > 0 and str[i] == str[i - 1]:
                continue
            chosen.append(str[i])
            # just construct a new input
            self.dfs(str[0:i] + str[i+1:], chosen, ans)
            chosen.pop()
        return

