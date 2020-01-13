class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        if not strs:
            return []
        key_2_group = {}
        for s in strs:
            sl = list(s)
            sl.sort()
            key = "".join(sl)
            if key not in key_2_group:
                key_2_group[key] = []
            key_2_group[key].append(s)
        result = []
        for group in key_2_group.values():
            if len(group) >= 2:
                result.extend(group)
        return result


if __name__ == '__main__':
    s = Solution()
    ans = s.anagrams(["","b",""])
    print(ans)