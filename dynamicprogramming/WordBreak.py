class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak2(self, s, dict):
        if not s and not dict:
            return True
        elif not s or not dict:
            return False

        slen = len(s)
        dp = [False] * (slen + 1)
        dp[0] = True
        for i in range(1, slen + 1):
            # loop through the words: n^2 where n is the length of string
            for j in range(i, 0, -1):
                if s[j-1:i] in dict and dp[j-1]:
                    dp[i] = True
                    break
        return dp[slen]

    def wordBreak(self, s, dict):
        if not s and not dict:
            return True
        elif not s or not dict:
            return False

        slen = len(s)
        dp = [False] * (slen + 1)
        dp[0] = True
        for i in range(1, slen + 1):
            # loop through the dict, n*w*L where w is the number of w and L is the average word length
            for word in dict:
                if len(word) > i:
                    continue
                dp[i] = word == s[i - len(word): i] and dp[i - len(word)]
                if dp[i]:
                    break
        return dp[slen]

