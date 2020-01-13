class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        if not s:
            return []
        return self._partition(s, {})

    def _partition(self, s, memo):
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return [[]]
        result = []
        for i in range(len(s)):
            pat = s[:i+1]
            if not self._is_palindrome(pat):
                continue
            for sub in self._partition(s[i+1:], memo):
                result.append([pat] + sub)
        memo[s] = result
        return result

    def _is_palindrome(self, s):
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True