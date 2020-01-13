from collections import defaultdict
class Solution:
    def longestStrChain(self, words) -> int:
        size = len(words)
        dp = [0] * (size)
        dp[0] = 1
        words.sort(key=lambda x: len(x))
        for i in range(1, size):
            curr = words[i]
            dp[i] = 1
            for j in reversed(range(i)):  # I only need to compare with words that have length shorter by one.
                if (len(words[i]) - len(words[j]) > 1):
                    break
                if self.chain(words[j], curr):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def chain(self, w1, w2):
        if len(w2) != len(w1) + 1:
            return False
        charCount = defaultdict(int)
        for c in w2:
            charCount[c] += 1
        for c in w1:
            if c not in charCount:
                return False
            charCount[c] -= 1
            if charCount[c] == 0:
                del charCount[c]
        return len(charCount) == 1 and sum(charCount.values()) == 1
