class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        start, end = self.find_closest_pair(A, target)
        result = []
        while k > 0:
            if self.is_left_closer(A, target, start, end):
                result.append(A[start])
                start -= 1
            else:
                result.append(A[end])
                end += 1
            k -= 1
        return result

    def find_closest_pair(self, A, target):
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                # don't do start = mid + 1. This is an error
                # the goal is not to find the target, the goal is to find
                # closest pair to the target
                # if we do start = mid + 1, we could have both start and end
                # in the same position
                start = mid  #
            else:
                end = mid
        return start, end

    def is_left_closer(self, A, target, start, end):
        if end >= len(A):
            return True
        if start < 0:
            return False
        return target - A[start] <= A[end] - target



class Solution2:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        start, end = self.find_closest_pair(A, target)
        result = []
        while k > 0:
            if self.is_left_closer(A, target, start, end):
                result.append(A[start])
                start -= 1
            else:
                result.append(A[end])
                end += 1
            k -= 1
        return result

    def find_closest_pair(self, A, target):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end) // 2
            if A[mid] == target:
                return mid, mid + 1
            elif A[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return end, start

    def is_left_closer(self, A, target, start, end):
        if end >= len(A):
            return True
        if start < 0:
            return False
        return target - A[start] <= A[end] - target

if __name__ == '__main__':
    Solution().kClosestNumbers([1,2,3], 2, 3)