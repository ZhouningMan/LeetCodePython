class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        if not A:
            return 0
        first = self.find_first_occurrence(A, target)
        if first == -1:
            return 0
        last = self.find_last_occurrence(A, target)
        return last - first + 1

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