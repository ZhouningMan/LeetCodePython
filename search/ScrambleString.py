class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """
    def isScramble(self, s1, s2):
        if not s1 or not s2:
            return False
        if len(s1) != len(s2):
            return False
        return self._isScramble(s1, s2, {})


    def _isScramble(self, s1, s2, memo):
        # always check the memo first
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        # if two strings are the same, they are scrambe of each other
        if s1 == s2:
            memo[(s1, s2)] = True
            return True
        for i in range(1, len(s1)):
            # don't swap the children
            if self._isScramble(s1[:i], s2[:i], memo) and self._isScramble(s1[i:len(s1)], s2[i:len(s2)], memo):
                memo[(s1, s2)] = True
                return True
            # swap the children
            # self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
            if self._isScramble(s1[:i], s2[-i:], memo) and self._isScramble(s1[i:], s2[:-i], memo):
                memo[(s1, s2)] = True
                return True
        memo[(s1, s2)] = False
        return False
