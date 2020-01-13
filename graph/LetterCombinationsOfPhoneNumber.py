
MAPPING = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []
        ans = []
        self.dfs(digits, 0, [], ans)
        return ans

    def dfs(self, digits, index, chosen, answers):
        if index == len(digits):
            answers.append("".join(chosen))
            return

        for c in MAPPING[int(digits[index])]:
            c = c.lower()
            chosen.append(c)
            self.dfs(digits, index + 1, chosen, answers)
            chosen.pop()

