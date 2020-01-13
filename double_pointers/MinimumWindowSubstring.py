class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source, target):
        if source is None or target is None:
            return ""

        freq_map = self.get_freq_map(target)
        j = 0
        left, right = 0, 0  # if there are no such window return ""
        size = len(source) + 1
        matched = 0
        for i, char in enumerate(source):
            while j < len(source) and matched < len(freq_map):
                if source[j] not in freq_map:
                    j += 1
                    continue
                if freq_map[source[j]] == 1:  # when we have reduce the freq to 1, we have match this char
                    matched += 1
                freq_map[source[j]] -= 1
                j += 1
            if matched == len(freq_map):  # valid window
                if j - i < size:  # we have a smaller window
                    left = i
                    right = j
                    size = j - i
            if char in freq_map:
                # we don't have any extra characters left, so when we remove one, we unmatch
                # a char
                if freq_map[char] == 0:
                    matched -= 1  # one less matched
                freq_map[char] += 1
        return source[left:right]

    def get_freq_map(self, s):
        freq_map = {}
        for c in s:
            freq_map[c] = freq_map.get(c, 0) + 1
        return freq_map

if __name__ == '__main__':
    print(Solution().minWindow("", ""))