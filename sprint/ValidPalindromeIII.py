
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        size = len(s)
        dp = [[0] * size for _ in range(size)]
        for le in range(2, size + 1):
            for start in range(0, size - le + 1):
                end = start + le - 1
                if s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end - 1] if le > 2 else 0
                else:
                    dp[start][end] = 1 + min(dp[start + 1][end], dp[start][end - 1])
        return dp[0][size -1] <= k


    def dfs(self, s, k, memo):
        valid = False
        if len(s) <= 1:
            valid = True
        elif k == 0:
            valid = s ==s[::-1]
        elif (s, k) in memo:
            return memo[(s, k)]
        else:
            i = 0
            j = len(s) - 1
            while i <= j and s[i] == s[j]:
                i += 1
                j -= 1
            if i >= j:
                valid = True
            else:
                valid = self.dfs(s[ i +1: j +1], k - 1, memo) or \
                        self.dfs(s[i:j], k - 1, memo)
        memo[(s, k)] = valid
        return valid


