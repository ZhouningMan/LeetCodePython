class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if not A:
            return False
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] == target:
                return True
            elif A[mid] == A[end]:
                end -= 1
            elif A[mid] > A[end]:
                if A[end] < target < A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                # don't forget the equal condition
                if A[mid] < target <= A[end]:
                    start = mid
                else:
                    end = mid
        return A[start] == target or A[end] == target

    def search2(self, A,  target):
        if not A:
            return -1
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end) // 2
            if A[mid] == target:
                return mid
            if target < A[mid]:
                #
                if target < A[start] <= A[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if A[mid] <= A[end] < target:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1

    def search3(self, A, target):
        if not A:
            return False
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end) // 2
            if A[mid] == target:  # special conditionfindMedian
                return True

            if A[mid] == A[end]:
                end -= 1
            elif A[mid] < A[end]:
                if A[mid] < target <= A[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if A[start] <= start < A[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return False



