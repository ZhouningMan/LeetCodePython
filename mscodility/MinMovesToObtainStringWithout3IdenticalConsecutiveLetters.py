class Solution:
    def min_moves(self, s):
        if not s:
            return 0
        moves = 0
        i = 0
        length = len(s)
        while i < length:
            count = 1
            j = i + 1
            while j < length and s[j] == s[i]:
                count += 1
                j += 1
            moves += count // 3
            # update the location of i to the end of the window
            i = j
        return moves


if __name__ == '__main__':
    s = Solution()
    inputs = ["baaaaa", "baaaaaa", "baaaab", "baaabbaabbba", "baabab", "bbaabbaabbabab"]
    expected = [1, 2, 1, 2, 0, 0]
    for i, e in zip(inputs, expected):
        real = s.min_moves(i)
        if real == e:
            print("Passed")
        else:
            print(f"{i}: {real}, expected : {e}")
