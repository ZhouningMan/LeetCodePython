import sys

class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        if divisor == 0:
            raise ZeroDivisionError("...")
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        q1, _ = self.divideRecur(abs(dividend), abs(divisor))
        return q1 if sign == 1 else -q1

    def divideRecur(self, dividend, divisor):
        if dividend < divisor:
            return 0, dividend
        left = dividend >> 1  # divide by 2
        # only do half the work
        q1, r1 = self.divideRecur(left, divisor)
        q1 <<= 1
        r1 = r1 + r1 + (dividend - left - left)
        # don't call recursion again, just do constant operations
        # i don't know whether if works, so just change to while, at the
        # worst, there are two iterations
        while r1 >= divisor:
            q1 += 1
            r1 -= divisor
        return q1, r1


if __name__ == '__main__':
    s = Solution()
    res = s.divide(2147483647, 1)
    print(res)