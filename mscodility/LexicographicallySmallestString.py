class Solution:
    def impl(self, s):
        if not s:
            raise ValueError("...")
        length = len(s)
        if length == 1:
            return ""
        to_remove = -1
        for i in range(1, length):
            if s[i] < s[i-1]:
                to_remove = i - 1
                break
            else:
                to_remove = i
        return s[:to_remove] + s[to_remove + 1:]

if __name__ == '__main__':
    s = Solution()
    ans = s.impl("abcde")
    print(ans)
