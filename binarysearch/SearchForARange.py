class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        if not A:
            return [-1, -1]
        first = self.find_first_occurrence(A, target)
        last = self.find_last_occurrence(A, target)
        return [first, last]

    def find_first_occurrence(self, A, target):
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        return -1

    def find_last_occurrence(self, A, target):
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            return end
        elif A[start] == target:
            return start
        return -1