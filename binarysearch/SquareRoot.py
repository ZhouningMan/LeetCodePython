class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x < 0:
            raise ValueError('....')
        # special case
        if x == 0 or x == 1:
            return x

        start, end = 0, x
        while start <= end:
            mid = start + (end - start) // 2
            # whenever you do division, think of division by zero
            quotient = x // mid
            if quotient == mid:
                return mid
            elif quotient > mid:
                start = mid + 1
            else:
                end = mid - 1
        # most of the time we return low because that is the insertion point,
        # but in this case if we return low, then low*low > x
        return end
