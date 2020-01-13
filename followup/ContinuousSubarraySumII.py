class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        if not A:
            return None
        m = len(A)
        max_sum, maxs, maxe = self.find_extreme(A, lambda x, y: x > y)
        min_sum, mins, mine = self.find_extreme(A, lambda x, y: x < y)
        total = sum(A)
        # There is a special case, when the min subarray contains the entire
        # array
        if max_sum >= total - min_sum or mine - mins + 1 == m:
            return [maxs, maxe]
        else:
            return [(mine + 1) % m, (mins + m - 1) % m]

    def find_extreme(self, A, predicate):
        i = 0
        local_extreme = A[0]
        extreme = local_extreme
        start = 0
        end = 0
        for j in range(1, len(A)):
            if predicate(A[j], local_extreme + A[j]):
                local_extreme = A[j]
                i = j
            else:
                local_extreme += A[j]
            # update global answer when a better candidate is found
            if predicate(local_extreme, extreme):
                start = i
                end = j
                extreme = local_extreme
        return extreme, start, end

if __name__ == '__main__':
    s = Solution()
    res = s.continuousSubarraySumII([-2,0,0,1,-1,-1])
    print(res)