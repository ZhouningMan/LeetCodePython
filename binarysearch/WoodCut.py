class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        if not L or len(L) == 0:
            return 0

        # pick a good start value
        start = 1
        end = max(L)
        while start <= end:
            mid = start + (end - start) // 2
            count = self.pieces(L, mid)
            if count < k:
                end = mid - 1
            else:
                start = mid + 1
        # return the end  not the start
        return end

    def pieces(self, L, length):
        count = 0
        for le in L:
            # anytime you do a division, make sure the divisor
            # is not equal to zero
            count += le // length
        return count

if __name__ == '__main__':
    s = Solution()
    print(dir(s))