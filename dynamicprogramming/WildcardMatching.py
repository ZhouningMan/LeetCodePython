class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    # def isMatch(self, s, p):
    #     slen = len(s)
    #     plen = len(p)
    #     dp = [[False for _ in range(slen + 1)] for _ in range(plen + 1)]
    #
    #     for pi in range(plen + 1):
    #         for si in range(slen + 1):
    #             if pi == si == 0:
    #                 dp[pi][si] = True
    #             elif si == 0:
    #                 dp[pi][si] = p[pi-1] == '*' and dp[pi-1][si]
    #             elif pi == 0:
    #                 dp[pi][si] = False
    #             else:
    #                 if p[pi-1] != '*':
    #                     dp[pi][si] = dp[pi-1][si-1] and (p[pi-1] == '?' or p[pi-1] == s[si-1])
    #                 else:
    #                     dp[pi][si] = dp[pi-1][si-1] or dp[pi-1][si] or dp[pi][si-1]
    #     return dp[plen][slen]

    def isMatch(self, s, p):
        slen = len(s)
        plen = len(p)

        # you can use string or pattern as the rolling row, it doesn't matter
        dp = [[False for _ in range(slen + 1)] for _ in range(2)]
        # you can loop through string first, or pattern first doesn't matter
        for pi in range(plen + 1):
            for si in range(slen + 1):
                if pi == si == 0:
                    dp[pi % 2][si] = True
                elif si == 0:
                    dp[pi % 2][si] = p[pi-1] == '*' and dp[(pi-1) % 2][si]
                elif pi == 0:
                    dp[pi % 2][si] = False
                else:
                    if p[pi-1] != '*':
                        dp[pi % 2][si] = dp[(pi-1) % 2][si-1] and (p[pi-1] == '?' or p[pi-1] == s[si-1])
                    else:
                        dp[pi % 2][si] = dp[(pi-1) % 2][si-1] or dp[(pi-1) % 2][si] or dp[pi % 2][si-1]
        return dp[plen % 2][slen]


    # def isMatch(self, s, p):
    #     slen = len(s)
    #     plen = len(p)
    #     dp = [[False for _ in range(plen + 1)] for _ in range(slen + 1)]
    #
    #     for si in range(slen + 1):
    #         for pi in range(plen + 1):
    #             if pi == si == 0:
    #                 dp[si][pi] = True
    #             elif si == 0:
    #                 dp[si][pi] = p[pi-1] == '*' and dp[si][pi-1]
    #             elif pi == 0:
    #                 dp[si][pi] = False
    #             else:
    #                 if p[pi-1] != '*':
    #                     dp[si][pi] = dp[si-1][pi-1] and (p[pi-1] == '?' or p[pi-1] == s[si-1])
    #                 else:
    #                     dp[si][pi] = dp[si-1][pi-1] or dp[si][pi-1] or dp[si-1][pi]
    #     return dp[slen][plen]


    # def isMatch(self, s, p):
    #     slen = len(s)
    #     plen = len(p)
    #     dp = [[False for _ in range(plen + 1)] for _ in range(2)]
    #
    #     for si in range(slen + 1):
    #         for pi in range(plen + 1):
    #             if pi == si == 0:
    #                 dp[si % 2][pi] = True
    #             elif si == 0:
    #                 dp[si % 2][pi] = p[pi-1] == '*' and dp[si % 2][pi-1]
    #             elif pi == 0:
    #                 dp[si % 2][pi] = False
    #             else:
    #                 if p[pi-1] != '*':
    #                     dp[si % 2][pi] = dp[(si-1) % 2][pi-1] and (p[pi-1] == '?' or p[pi-1] == s[si-1])
    #                 else:
    #                     dp[si % 2][pi] = dp[(si-1) % 2][pi-1] or dp[si % 2][pi-1] or dp[(si-1) % 2][pi]
    #     return dp[slen%2][plen]


if __name__ == '__main__':
    s = Solution()
    s.isMatch("aa" ,"a")