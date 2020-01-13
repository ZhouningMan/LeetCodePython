class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        if not s or not dict:
            return 0
        s = s.lower()
        dict = [v.lower() for v in dict]
        slen = len(s)
        dp = [0] * (slen + 1)
        # for empty s, we can find an empty sentence.
        # This is just in the context of DP.
        dp[0] = 1
        for i in range(1, slen + 1):
            for j in range(0, i):
                sub = s[j: i]
                if sub in dict:
                    dp[i] += dp[j]
        return dp[slen]