class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.find_kth(A, 0, B, 0, n // 2 + 1)
        else:
            return (self.find_kth(A, 0, B, 0, n // 2) + self.find_kth(A, 0, B, 0, n // 2 + 1)) / 2

    # all kth numbers are all 1-based
    # find kth numbers in items made from A[a_start:-1] and B[b_start:-1]
    def find_kth(self, A, a_start, B, b_start, k):
        if len(A) == a_start:
            return B[b_start + k - 1]
        if len(B) == b_start:
            return A[a_start + k - 1]
        if k == 1:
            return min(A[a_start], B[b_start])
        # a is none means A cannot contribute half of k, so B definitely needs to contribute
        # half k
        a = A[a_start + k//2 - 1] if a_start + k//2 - 1 < len(A) else None
        b = B[b_start + k//2 - 1] if b_start + k//2 - 1 < len(B) else None
        if a is None or (b is not None and a > b):
            return self.find_kth(A, a_start, B, b_start + k//2, k - k//2)
        else:
            return self.find_kth(A, a_start + k//2, B, b_start, k - k//2)

    def findMedianSortedArraysByResult(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.find_kth_smallest(A, B, n // 2 + 1) # K is 1 based
        else:
            return self.find_kth_smallest(A, B, n // 2) + self.find_kth_smallest(A, B, n // 2 + 1)

    def find_kth_smallest(self, A, B, k):
        start, end = self.find_range(A, B)
        while start <= end:
            if start == end:
                return start
            mid = (start + end) // 2

