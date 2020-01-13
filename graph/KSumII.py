class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        if not A or k <= 0:
            return []
        A.sort()
        ans = []
        self.dfs(A, k, target, 0, [], ans)
        return ans

    def dfs(self, A, k, target, index, chosen, ans):
        if k == 0:
            if target == 0:
                ans.append(list(chosen))
            return
        if index == len(A):
            return  # not possible
        if A[index] > target:
            return  # not possible
        # do not pick ith number
        self.dfs(A, k, target, index + 1, chosen, ans)
        # pick ith number
        chosen.append(A[index])
        self.dfs(A, k - 1, target - A[index], index + 1, chosen, ans)
        chosen.pop()

