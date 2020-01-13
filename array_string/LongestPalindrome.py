from collections import defaultdict
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        if not s:
            return 0
        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1
        odd = False
        length = 0
        for _, v in char_freq.items():
            if v % 2 == 0:
                length += v
            else:
                # take even numbers from the odd number
                length += (v // 2) * 2
                odd = True
        if odd:
            length += 1
        return length

if __name__ == '__main__':
    s = Solution()
    v = "NTrQdQGgwtxqRTSBOitAXUkwGLgUHtQOmYMwZlUxqZysKpZxRoehgirdMUgy"
    res = s.longestPalindrome(v)
    print(res)