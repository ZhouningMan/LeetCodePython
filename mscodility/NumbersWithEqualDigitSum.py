class Solution:
    def max_sum_when_digit_sum_equals(self, nums):
        if not nums:
            return -1
        ans = -1
        digit_sum_2_num = {}
        for num in nums:
            # find the sum of digits
            digit_sum = self.sum_digit(num)
            # check if we have seen it before or not
            if digit_sum in digit_sum_2_num:
                prev = digit_sum_2_num[digit_sum]
                ans = max(ans, num + prev)
                # only save the bigger value for a digit sum key
                if num > prev:
                    digit_sum_2_num[digit_sum] = num
            else:
                digit_sum_2_num[digit_sum] = num
        return ans

    def sum_digit(self, num):
        s = 0
        while num:
            s += num % 10
            num //= 10
        return s

if __name__ == '__main__':
    s = Solution()
    print(s.max_sum_when_digit_sum_equals([51,  71,17,  80, 42]))
    print(s.max_sum_when_digit_sum_equals([42, 33, 60]))
    print(s.max_sum_when_digit_sum_equals([51, 32, 43]))