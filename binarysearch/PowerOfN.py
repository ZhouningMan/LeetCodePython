class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        if n < 0:
            return self.pow(1/x, abs(n))
        else:
            return self.pow(x, n)

    def pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        half = self.pow(x, n // 2)
        return half * half * self.pow(x, n % 2)

    def myPow2(self, x, n):  # Note:在Python3中整除需使用"//"
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        tmp = x

        while n != 0:
            if n % 2 == 1:
                # 1 + 2 + 4 + 8
                ans *= tmp
            tmp *= tmp
            n = n // 2
        return ans

if __name__ == '__main__':
    s = Solution()
    ans = s.myPow2(4, 7)