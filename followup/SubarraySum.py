class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        if not nums:
            return None
        sum_2_idx = {}
        pre_sum = 0
        for i, num in enumerate(nums):
            pre_sum += num
            if pre_sum == 0:
                return [0, i]
            elif pre_sum in sum_2_idx:
                begin = sum_2_idx[pre_sum] + 1
                return [begin, i]
            sum_2_idx[pre_sum] = i
        return None


if __name__ == '__main__':
    s = Solution()
    res = s.subarraySum([1,0,1])
    print(res)