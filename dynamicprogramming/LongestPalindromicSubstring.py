class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome2(self, s):
        if not s:
            return ""
        # dp[i][j]: whether s[i:j] are palindromic
        # dp[i][j]: dp[i][j] = True if s[i] == s[j] and dp[i+1][j-1]
        m = len(s)
        dp = [[False] * m for _ in range(m)]
        left, right = -1, -1
        for length in range(1, m + 1):
            for start in range(m + 1 - length):
                end = start + length - 1
                if length == 1:
                    dp[start][end] = True
                elif length == 2:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = s[start] == s[end] and dp[start + 1][end - 1]
                if end - start >= right - left and dp[start][end]:
                    left, right = start, end
        return s[left: right + 1]

    def longestPalindrome(self, s):
        if not s:
            return ""
        m = len(s)
        if m == 1:
            return s
        start = 0
        end = 0
        length = 1
        for i in range(m-1):
            for c1, c2 in [(i, i), (i, i + 1)]:
                s1, e1 = self.expand(s, c1, c2)
                if e1 - s1 + 1 > length:
                    start, end = s1, e1
                    length = e1 - s1 + 1
        return s[start: end + 1]

    def expand(self, s, c1, c2):
        while c1 >= 0 and c2 < len(s):
            if s[c1] != s[c2]:
                break
            c1 -= 1
            c2 += 1
        return c1 + 1, c2 - 1

if __name__ == '__main__':
    s = Solution()
    s.longestPalindrome("ccc")