class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        if not s or not p:
            return False
        slen = len(s)
        plen = len(p)
        dp = [[False for _ in range(slen + 1)] for _ in range(plen + 1)]
        for pi in range(plen + 1):
            for si in range(slen + 1):
                if pi == 0 and si == 0:
                    dp[pi][si] = True
                elif si == 0:
                    if pi >= 2:
                        # don't confused the character index with length
                        dp[pi][si] = p[pi-1] == '*' and p[pi-2] != '*' and dp[pi-2][si]
                    else:
                        dp[pi][si] = False
                elif pi == 0:
                    dp[pi][si] = False
                else:
                    if p[pi-1] != '*':
                        dp[pi][si] = self.match_char(s, p, si, pi) and dp[pi-1][si-1]
                        continue
                    # we have a wildcard
                    if pi == 1:
                        dp[pi][si] = False
                    else:
                        # three conditions
                        # wildcard don't match any character
                        # wildcard character TRYING to match a single character, basically no wildcard
                        # wildcard matches more than one character given it matches
                        dp[pi][si] = dp[pi-2][si] \
                                        or dp[pi-1][si] \
                                        or (self.match_char(s, p, si, pi-1) and dp[pi][si-1])
        return dp[plen][slen]

    def match_char(self, s, p, si, pi):
        return s[si-1] == p[pi-1] or p[pi-1] == '.'

    def isMatch2(self, s, p):
        if not s or not p:
            return False
        slen = len(s)
        plen = len(p)
        dp = [[False for _ in range(slen + 1)] for _ in range(2)]
        for pi in range(plen + 1):
            for si in range(slen + 1):
                if pi == 0 and si == 0:
                    dp[pi%2][si] = True
                elif si == 0:
                    if pi >= 2:
                        # don't confused the character index with length
                        dp[pi%2][si] = p[pi-1] == '*' and p[pi-2] != '*' and dp[(pi-2)%2][si]
                    else:
                        dp[pi%2][si] = False
                elif pi == 0:
                    dp[pi%2][si] = False
                else:
                    if p[pi-1] != '*':
                        dp[pi%2][si] = self.match_char(s, p, si, pi) and dp[(pi-1)%2][si-1]
                        continue
                    # we have a wildcard
                    if pi == 1:
                        dp[pi%2][si] = False
                    else:
                        # three conditions
                        # wildcard don't match any character
                        # wildcard character TRYING to match a single character, basically no wildcard
                        # wildcard matches more than one character given it matches
                        dp[pi%2][si] = dp[(pi-2)%2][si] \
                                        or dp[(pi-1)%2][si] \
                                        or (self.match_char(s, p, si, pi-1) and dp[pi%2][si-1])
        return dp[plen%2][slen]


if __name__ == '__main__':
    s = Solution()
    s.isMatch("bbbba", ".*a*a")
