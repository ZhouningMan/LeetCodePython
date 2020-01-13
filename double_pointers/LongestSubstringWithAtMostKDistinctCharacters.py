class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if s is None:
            return 0
        n = len(s)
        freq_map = {}
        j = 0
        size = 0
        for i, char in enumerate(s):
            while j < n and len(freq_map) <= k:
                # the goal is to make sure [i, j) contains k distinct characters
                if len(freq_map) == k and s[j] not in freq_map:
                    # so we shouldn't add the new element to the map if that is breaking our condition
                    break
                freq_map[s[j]] = freq_map.get(s[j], 0) + 1
                j += 1

            size = max(size, j - i)
            # to deal with looking for empty character probelm
            if char not in freq_map:
                continue
            freq_map[char] -= 1
            if freq_map[char] == 0:
                del freq_map[char]
        return size


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstringKDistinct("asdfdW", 0))