class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        if not s:
            # empty string is considered palindrome
            return True
        i = 0
        j = len(s) - 1
        while i <= j:
            # python like simplicity, so the name
            # all simples
            while i <= j and not s[i].isalnum():
                i += 1
            while i <= j and not s[j].isalnum():
                j -= 1
            if i <= j:
                left = s[i].lower()
                right = s[j].lower()
                if left != right:
                    return False
                i += 1
                j -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    res = s.isPalindrome("A man, a plan, a canal: Panama")
    print(res)