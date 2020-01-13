
class Match:
    def __init__(self, begin, end, match):
        self.begin = begin
        self.end = end
        self.match = match


MISMATCH = Match(-1, -1, False)


class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    # def wordPatternMatch(self, pattern, str):
    #     if not pattern or not str:
    #         return False
    #     idx_map = {}
    #     slen = len(str)
    #     plen = len(pattern)
    #     for i in reversed(range(plen)):
    #         idx_map[pattern[i]] = i # first index
    #
    #     dp = [[MISMATCH for _ in range(plen)]]
    #     for pi in range(plen):
    #         for si in range(slen):
    #             if pi == 0:
    #                 dp[pi] = Match(0, si, True)
    #                 continue
    #             first_idx = idx_map[pattern[pi]]
    #             prev = dp[pi-1]
    #             if prev.match:
    #                 curr = Match(prev.end + 1, si, True)
    #             else:
    #                 curr = MISMATCH
    #             if pi == first_idx:
    #                 dp[pi] = curr
    #                 continue
    #
    #             first_match = dp[first_idx]
    #             if first_match.match and curr.match:
    #                 dp[pi] = curr if self.same_pattern(str, first_match, curr) else MISMATCH
    #             else:
    #                 dp[pi] = MISMATCH
    #
    #     return dp[plen-1].match


    def wordPatternMatch(self, pattern, str):
        if not pattern or not str:
            return False
        return self.is_match(pattern, str, {}, set())

    def is_match(self, pattern, s, mapping, used):
        plen = len(pattern)
        slen = len(s)
        if plen == 0 and slen == 0:
            return True
        elif plen == 0 or slen == 0:
            return False
        pc = pattern[0]
        if pc in mapping:
            prev = mapping[pc]
            if s.startswith(prev):
                return self.is_match(pattern[1:], s[len(prev):], mapping, used)
            else:
                return False
        # this is new character
        for i in range(slen):
            pat = s[:i + 1]
            if pat in used:
                continue
            used.add(pat)
            mapping[pc] = pat
            if self.is_match(pattern[1:], s[i+1:], mapping, used):
                return True
            del mapping[pc]
            used.remove(pat)
        return False


if __name__ == '__main__':
    s = Solution()
    s.wordPatternMatch("abba", "redbluebluered")
