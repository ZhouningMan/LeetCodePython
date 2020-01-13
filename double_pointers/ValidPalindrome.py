class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        if not s:
            return True
        i, j = self.check(s)
        if i >= j:
            return True
        return self.isValid(s[i:j]) or self.isValid(s[i+1:j+1])

    def isValid(self, s):
        i, j = self.check(s)
        if i >= j:
            return True
        return False

    def check(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return i, j
            i += 1bo
            j -= 1ra
        return i, j