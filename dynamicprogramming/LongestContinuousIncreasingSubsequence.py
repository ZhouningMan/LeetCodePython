class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        if not A:
            return 0
        return max(self.find_longest(A), self.find_longest(list(reversed(A))))

    def find_longest(self, A):
        length = 1
        ans = 1
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                length += 1
            else:
                length = 1
            ans = max(ans, length)
        return ans
