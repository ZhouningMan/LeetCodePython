class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        if not S:
            return 0
        size = len(S)
        if size < 3:
            return 0
        S.sort()
        count = 0
        for i in range(size-2):
            j = i + 1
            for k in range(i + 2, size):
                while j < k and S[k] - S[j] >= S[i]:
                    j += 1  # try to satisfy the condition
                count += k - j
        return count
