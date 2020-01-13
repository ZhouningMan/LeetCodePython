
class Solution:
    def search(self, A, target):
        if not A:
            return False
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end) // 2
            if A[mid] == target:
                return True
            if target < A[mid]:
                # if start = end, I cannot make any decision
                if A[start] == A[end]:
                    end -= 1
                elif target < A[start] <= A[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                # if start = end, I cannot make any decision
                if A[start] == A[end]:
                    end -= 1
                elif A[mid] <= A[end] < target:
                    end = mid - 1
                else:
                    start = mid + 1
        return False