class Solution:
    def longest(self, s):
        if not s:
            return 0
        length = len(s)
        if length < 3:
            return length
        start, end = 0, 2
        j = 0
        for i in range(2, length):
            if s[i] == s[i-1] == s[i-2]:
                if i - j > end - start:
                    start, end = j, i
                j = i - 2
        if length - j > end - start:
            start, end = j, length
        return s[start:end]

if __name__ == '__main__':
    s = Solution()
    inputs = ["aabbaaaaabb", "aabbaabbaabbaa"]
    expected = ["aabbaa", "aabbaabbaabbaa"]
    for i, e in zip(inputs, expected):
        real = s.longest(i)
        if real == e:
            print("Passed")
        else:
            print(f"{i}: {real}, expected : {e}")