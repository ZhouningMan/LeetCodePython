class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumIIWrong(self, A, start, end):
        if not A:
            return 0
        m = len(A)
        s = 0
        e = s
        range_sum = 0  # [start, end]
        count = 0
        # This is the wrong solution, there are at most O(n^2) answers.
        # and with this double pointer, you only increment by one, so the
        # count is at most O(N)
        for e in range(m):
            range_sum += A[e]
            while range_sum > end and s <= e:
                range_sum -= A[s]
                s += 1
            if s <= e and range_sum >= start:
                count += 1
        while s <= e and range_sum >= start:
            count += 1
            range_sum -= A[s]
            s += 1
        return count

    def subarraySumII(self, A, start, end):
        if not A:
            return 0
        if end <= 0:
            return 0
        m = len(A)
        # how to deal with boundary condition ?
        left_sum = 0
        right_start_sum, right_start_idx = 0, 0
        right_end_sum, right_end_idx = 0, 0
        count = 0
        # how three pointers work here?
        # we fix left and then try to maximize the number of subarray that fix the conditions
        # the number of possible solutions will keep decreasing as we move left pointer to right
        # Basically, any subarray within this range [left, right_start_idx -1 ... right_end_idx - 1]
        # will fall into the interval
        for left in range(m):
            # as we move left to right, left_sum will keep increasing, so we have to move right_start_idx to
            # satisfy our condition
            while right_start_sum - left_sum < start and right_start_idx < m:
                right_start_sum += A[right_start_idx]
                right_start_idx += 1 # next index
            # we have move left pointer so we increase the left_sum, therefore, we have to move
            # right_end_idx to the right
            while right_end_idx < m and right_end_sum + A[right_end_idx] - left_sum <= end :
                right_end_sum += A[right_end_idx]
                right_end_idx += 1
            # how do we deal with corner case, remember all we care is that we have a valid answer.
            if start <= right_start_sum - left_sum <= end:
                count += right_end_idx - right_start_idx + 1
            # we want to A[left] after the iteration because the region that satisfy the condition is left inclusive
            # [left, right_start_idx -1 ... right_end_idx - 1]
            left_sum += A[left]
        return count

if __name__ == '__main__':
    s = Solution()
    res = s.subarraySumII([1,2,3,4], 1, 3)
    print(res)