import sys

class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame2(self, A):
        if not A or len(A) < 2:
            return 0
        alen = len(A)
        # straighten the circled list
        dp = [[0 for _ in range(alen * 2 - 1)] for _ in range(alen * 2 - 1)]
        pre_sum = self.prefix_sum(A)
        # the circle list has effective lenght of alen
        for length in range(2, alen + 1):
            # we need to loop through the entire straightened list because
            # i was doing something long by only looping through range(0, alen)
            for start in range(0, alen * 2 - length):
                end = start + length - 1
                dp[start][end] = sys.maxsize
                for mid in range(start, end):
                    last_sum = pre_sum[end] if start == 0 else pre_sum[end] - pre_sum[start - 1]
                    dp[start][end] = min(dp[start][end], last_sum + dp[start][mid] + dp[mid+1][end])
        result = sys.maxsize
        for i in range(0, alen):
            result = min(result, dp[i][i + alen - 1])
        return result

    def prefix_sum(self, A):
        A = A + A[:-1]
        alen = len(A)
        pre_sum = [0] * alen
        pre_sum[0] = A[0]
        for i in range(alen):
            pre_sum[i] = A[i] + pre_sum[i - 1]
        return pre_sum

if __name__ == '__main__':
    s = Solution()
    res = s.stoneGame2([3,4,3])
    print(res)