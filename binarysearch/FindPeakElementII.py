class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        n = len(A[0])
        start, end = 0, n - 1

        # Instead of find the local peak, we try to find the
        # global peak, which is mlogn
        while start <= end:
            mid = (start + end) // 2
            # return the max index of this column
            r = self._find_max(A, mid)
            # if the left value is greater than the max value in the
            # mid column, the result is on the left
            if mid - 1 >= 0 and A[r][mid-1] > A[r][mid]:
                end = mid - 1
            # similarly, the result is on the right
            elif mid + 1 < n and A[r][mid+1] > A[r][mid]:
                start = mid + 1
            else:
                return [r, mid]
        return [-1, -1]

    def _find_max(self, A, col):
        idx = 0
        for r in range(1, len(A)):
            if A[r][col] > A[idx][col]:
                idx = r
        return idx

