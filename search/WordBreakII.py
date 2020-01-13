class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return []
        res = self.collect(s, wordDict, {})
        return [" ".join(li) for li in res]

    # identify the subproblem is the key to any DFS
    def collect(self, s, words, mappings):
        if len(s) == 0:
            # This is the key, return [[]] means we have
            # a subresult [], which just don't have any content
            # which is different from [] which means we don't have a solution
            return [[]]

        if s in mappings:
            return mappings[s]

        result = []
        for i in range(len(s)):
            pat = s[0: i + 1]
            if pat not in words:
                continue
            subresult = self.collect(s[i+1:], words, mappings)
            for li in subresult:
                result.append([pat] + li)
        mappings[s] = result
        return result

    # def is_possible(self, s, words):
    #     slen = len(s)
    #     dp = [False] * (slen + 1)
    #     dp[0] = True
    #     for i in range(1, slen + 1):
    #         # loop through the dict, n*w*L where w is the number of w and L is the average word length
    #         for word in words:
    #             if len(word) > i:
    #                 continue
    #             dp[i] = word == s[i - len(word): i] and dp[i - len(word)]
    #             if dp[i]:
    #                 break
    #     return dp[slen]


if __name__ == '__main__':
    s = Solution()
    res = s.wordBreak("aaaaaaaa", ["aaaa","aa","a"])
    print(res)