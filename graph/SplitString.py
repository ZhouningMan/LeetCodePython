class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        if not s:
            return [[]]
        ans = []
        self.dfs(s, 0, [], ans)
        return ans

    def dfs(self, s, index, chosen, answers):
        size = len(s)
        if index == size:
            answers.append(list(chosen))
            return

        for delta in [1, 2]:
            nextIdx = index + delta
            if nextIdx <= size:
                chosen.append(s[index:nextIdx])
                self.dfs(s, nextIdx, chosen, answers)
                chosen.pop()