class Solution:
    def impl(self, s):
        new_s = ""
        a_count = 0
        total = 0
        for c in s:
            if c == 'a':
                a_count += 1
            else:
                total += 2 - a_count
                a_count = 0
            if a_count > 2:
                return -1
        total += 2 - a_count
        return total


if __name__ == '__main__':
    s = Solution()
    print(s.impl("baaa"))

