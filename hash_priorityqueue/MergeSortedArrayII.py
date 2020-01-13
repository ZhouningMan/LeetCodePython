class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        k = m + n - 1
        m = m - 1
        n = n - 1
        while k >= 0:
            if m < 0:
                A[k] = B[n]
                n -= 1
            elif n < 0:
                A[k] = A[m]
                m -= 1
            elif A[m] < B[n]:
                A[k] = B[n]
                n -= 1
            else:
                A[k] = A[m]
                m -= 1
            k -= 1
