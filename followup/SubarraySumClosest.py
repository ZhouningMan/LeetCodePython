import sys
import collections

Pair = collections.namedtuple("Pair", ["sum", "index"])

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        if not nums:
            return None
        sum_2_idx = []
        pre_sum = 0
        for i, num in enumerate(nums):
            pre_sum += num
            sum_2_idx.append(Pair(pre_sum, i))
        sum_2_idx.sort()
        # always use absolute value for difference
        diff = abs(sum_2_idx[0].sum)
        start = 0
        end = sum_2_idx[0].index
        for i in range(1, len(sum_2_idx)):
            # don't shy away from using local variable
            new_diff = sum_2_idx[i].sum - sum_2_idx[i-1].sum
            if new_diff < diff:
                idx1 = sum_2_idx[i].index
                idx2 = sum_2_idx[i-1].index
                start = min(idx1, idx2) + 1
                end = max(idx1, idx2)
                diff = new_diff
        return [start, end]


if __name__ == '__main__':
    s = Solution()
    res = s.subarraySumClosest([-3,1,1,-3,5])
    print(res)