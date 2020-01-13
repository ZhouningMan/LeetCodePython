class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        if x < 0:
            raise ValueError("...")
        if x == 0:
            return 0

        # this is the key
        start, end = 0, max(x, 1)
        error = 0.0000000001
        while start <= end - error:
            mid = (start + end) / 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                end = mid
            else:
                start = mid
        return end

