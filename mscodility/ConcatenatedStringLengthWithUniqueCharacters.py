class Solution:
    def impl(self, A):
        size, count = self.dfs(set(), 0, 0, A)
        if count > 1:
            return size
        else:
            return 0

    def dfs(self, chosen, count, index, A):
        size = len(chosen)
        strings = count
        for i in range(index, len(A)):
            char_set = set(A[i])
            # the word itself must not contain duplicate
            if len(char_set) != len(A[i]) or not chosen.isdisjoint(char_set):
                continue
            # union both sets
            chosen |= char_set
            tmp_size, tmp_count = self.dfs(chosen, count + 1, i + 1, A)
            # since we are looking for concatenation,
            # we need at least two strings.
            if tmp_count > 1 and tmp_size > size:
                size = tmp_size
                strings = tmp_count
            chosen -= char_set
        return size, strings


if __name__ == '__main__':
    s = Solution()
    ans = s.impl(["co","dil","ity"])
    print(ans)