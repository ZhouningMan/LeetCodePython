class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        l = len(s1)
        m = len(s2)
        n = len(s3)
        if n != l + m:
            return False
        # dp[i][j]: whether s1[0:i] + s2[0:j] forms s3[0:i + j]
        # there are three variables, but only 2 are driving variables
        # dp[i][j] = (s1[i-1] == s3[k] and dp[i-1][j]) or (s2[j-1] == s3[k] and dp[i][j-1])
        dp = [[False] * (m + 1) for _ in range(l + 1)]

        for i in range(l + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    dp[0][0] = True
                elif i == 0:
                    dp[i][j] = s2[j-1] == s3[j-1] and dp[i][j-1]
                elif j == 0:
                    dp[i][j] = s1[i-1] == s3[i-1] and dp[i-1][j]
                else:
                    k = i+j-1
                    dp[i][j] = (s1[i-1] == s3[k] and dp[i-1][j]) or (s2[j-1] == s3[k] and dp[i][j-1])
        return dp[l][m]

    def isInterleaveOptimized(self, s1, s2, s3):
        l = len(s1)
        m = len(s2)
        n = len(s3)
        if n != l + m:
            return False
        # dp[i][j]: whether s1[0:i] + s2[0:j] forms s3[0:i + j]
        # dp[i][j] = False if s1[i-1] != s3[i+j-1] and s2[j-1] != s3[i+j-1]
        dp = [False] * (m + 1)

        for i in range(l + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    dp[0] = True
                elif i == 0:
                    dp[j] = s2[j - 1] == s3[j - 1] and dp[j - 1]
                elif j == 0:
                    dp[j] = s1[i - 1] == s3[i - 1] and dp[j]
                else:
                    k = i + j - 1
                    dp[j] = (s1[i - 1] == s3[k] and dp[j]) or (s2[j - 1] == s3[k] and dp[j - 1])
        return dp[m]


if __name__ == '__main__':
    s = Solution()
    s.isInterleave("a", "", "a")
