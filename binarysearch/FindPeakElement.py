class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        if not A:
            return -1
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid
        return start if A[start] > A[end] else end


    def findPeak2(self, A):
        if not A:
            return -1
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end) // 2
            # this is the special case where we exit.
            if mid == end:
                return end
            if A[mid] < A[mid + 1]:
                start = mid + 1
            else: # if A[mid] >= A[mid + 1], then mid could be a peak
                end = mid
        return end