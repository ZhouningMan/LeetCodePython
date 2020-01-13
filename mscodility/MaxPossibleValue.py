FIVE = '5'
class Solution:
    def max_possible_value(self, n):
        negative = n < 0
        digits = str(abs(n))
        new_num = ""
        inserted = False
        for d in digits:
            if inserted:
                new_num += d
                continue
            if negative and d > FIVE:
                new_num += FIVE
                inserted = True
            if not negative and d < FIVE:
                new_num += FIVE
                inserted = True
            new_num += d
        value = int(new_num)
        return -value if negative else value

if __name__ == '__main__':
    s = Solution()
    print(s.max_possible_value(-999))