class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        if s is None or len(s) == 0:
            return 0
        j = 0
        length = len(s)
        uniq = set()  # unique characters from [i, j)
        size = 0
        for i in range(length):
            while j < length and s[j] not in uniq:
                uniq.add(s[j])
                j += 1
            size = max(size, j - i)  # doesn't matter how we exit the condition
            # let the outer loop drive the removal of tail elements
            uniq.remove(s[i])  # keep removing until our condition is met
        return size

