class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        size = len(A)

        # dp[i] contains all longest Arithmetic subsequence ended at ith value
        # with various difference
        # dp[i] ==> {diff: count}
        dp = [None] * size
        ans = 1
        dp[0] = {}
        for i in range(1, size):
            dp[i] = {}
            for j in range(0, i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    count = dp[j][diff]
                else:
                    count = 1  # no previous diff, just jth value
                count += 1  # including ith value
                dp[i][diff] = count
                ans = max(ans, count)
        return ans