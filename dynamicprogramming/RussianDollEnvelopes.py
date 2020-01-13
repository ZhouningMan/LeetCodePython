import bisect

class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        m = len(envelopes)

        # reverse the sorting position of the height allows us
        # to use the height to determine whether later doll can fit
        # previous one if current height > previous height(when both height and width are the
        # same, the binary search will put that in the left, so we are fine)
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        size = 1
        dp = [0] * m
        # initialize the first value
        # dp[size - 1] stores the last element of the longest sequence
        # new sequence will only be longer if the new element is greater than biggest element of previous
        # longest sequence.
        dp[0] = envelopes[0][1]
        for env in envelopes:
            # we use bisect_left to avoid when both width and height are the same problem
            # we need to specify the range for the binary serach
            insertion = bisect.bisect_left(dp, env[1], 0, size)
            dp[insertion] = env[1]
            if insertion == size:
                size += 1
        return size


if __name__ == '__main__':
    s = Solution()
    res = s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])
    print(res)