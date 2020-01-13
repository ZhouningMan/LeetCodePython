class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """
    def numDecodings(self, s):
        if not s:
            return 0
        m = len(s)
        # dp[i] means starting from position i to the end, how many
        # ways to decode the string
        dp = [0] * (m + 1)
        dp[m] = 1  # special case for 1D array
        limit = 10**9 + 7
        for i in reversed(range(m)):
            if s[i] == '0':
                dp[i] = 0
            elif i == m - 1:
                dp[i] = 1 if s[i] != '*' else 9
            elif s[i] == '*' and s[i+1] == '*':
                dp[i] = 15 * dp[i+2] + 9 * dp[i+1]
            elif s[i+1] == '*':
                if s[i] == '1':
                    dp[i] = 9 * dp[i+2] + dp[i+1]
                elif s[i] == '2':
                    dp[i] = 6 * dp[i+2] + dp[i+1]
                else:
                    dp[i] = dp[i+1]
            elif s[i] == '*':
                dp[i] = 9 * dp[i+1]
                if s[i+1] > '6':
                    dp[i] += dp[i+2]
                else:
                    dp[i] += 2 * dp[i+2]
            else:
                dp[i] = dp[i + 1] if int(s[i:i + 2]) > 26 else dp[i + 1] + dp[i + 2]
        return dp[0] % limit

    def numDecodings2(self, s):
        if not s:
            return 0
        m = len(s)
        # dp[i] means starting from position i to the end, how many
        # ways to decode the string
        dp = [0] * 3
        dp[m%3] = 1  # special case for 1D array
        limit = 10**9 + 7
        for i in reversed(range(m)):
            if s[i] == '0':
                dp[i%3] = 0
            elif i == m - 1:
                dp[i%3] = 1 if s[i] != '*' else 9
            elif s[i] == '*' and  s[i+1] == '*':
                dp[i%3] = 15 * dp[(i+2)%3] + 9 * dp[(i+1)%3]
            elif s[i+1] == '*':
                if s[i] == '1':
                    dp[i%3] = 9 * dp[(i+2)%3] + dp[(i+1)%3]
                elif s[i] == '2':
                    dp[i%3] = 6 * dp[(i+2)%3] + dp[(i+1)%3]
                else:
                    dp[i%3] = dp[(i+1)%3]
            elif s[i] == '*':
                dp[i%3] = 9 * dp[(i+1)%3]
                if s[i+1] > '6':
                    dp[i%3] += dp[(i+2)%3]
                else:
                    dp[i%3] += 2 * dp[(i+2)%3]
            else:
                dp[i%3] = dp[(i + 1)%3] if int(s[i:i + 2]) > 26 else dp[(i + 1)%3] + dp[(i + 2)%3]
        return dp[0] % limit