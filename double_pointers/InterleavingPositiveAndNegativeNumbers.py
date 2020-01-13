class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        if not A:
            return
        # first partition to negative and positive
        # [0:i] negative, [i+1, len(A)- 1] positive
        i = self.partition(A)
        if i + 1 < len(A) - i - 1:
            # if we have less negative, the 0th index should be positive
            # +-+-+
            start = 0
        else:
            # negative count are not less than positive count
            # -+-+-+
            start = 1
        # merge step
        pos_idx = i + 1
        for i in range(start, len(A), 2):
            # just follow the order we have layout
            # as we are replacing more elements, more and more negatives are being
            # pushed to the end, so we just need to pick positive from right
            if A[i] < 0:  # this is an optional step
                A[i], A[pos_idx] = A[pos_idx], A[i]
                pos_idx += 1

    def partition(self, A):
        i = 0
        j = len(A) - 1
        while i <= j:
            if A[i] < 0:
                i += 1
            else:
                A[i], A[j] = A[j], A[i]
                j -= 1
        return j

if __name__ == '__main__':
    s = Solution()
    A = [26,-31,10,-29,17,18,-24,-10]

    s.rerange(A)
    print(A)
