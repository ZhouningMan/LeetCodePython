class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        if not s:
            return 0
        m = len(s)
        # dp[i] means starting from position i to the end, how many
        # ways to decode the string
        dp = [0] * (m + 1)
        dp[m] = 1  # special case for 1D array
        for i in reversed(range(m)):
            if s[i] == '0':
                dp[i] = 0
            elif i == m -1:
                dp[i] = 1
            else:
                dp[i] = dp[i+1] if int(s[i:i+2]) > 26 else dp[i+1] + dp[i+2]
        return dp[0]