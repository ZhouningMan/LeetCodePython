
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        if not A:
            return None
        sub_sum = A[0]
        i = 0
        max_sum = sub_sum
        start = 0
        end = 0
        for j in range(1, len(A)):
            if sub_sum + A[j] < A[j]:
                sub_sum = A[j]
                i = j
            else:
                sub_sum += A[j]
            # update global answer when a better candidate is found
            if sub_sum > max_sum:
                start = i
                end = j
                max_sum = sub_sum
        return [start, end]

if __name__ == '__main__':
    s = Solution()
    res = s.continuousSubarraySum([-2,0,0,1,-1,-1])
    print(res)