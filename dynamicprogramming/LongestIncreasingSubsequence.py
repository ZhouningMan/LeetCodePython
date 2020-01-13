import bisect


class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0
        m = len(nums)
        dp = [1] * m
        for i in range(m):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

    def longestIncreasingSubSequenceResult(self, nums):
        if nums is None or not nums:
            return 0

        # state: dp[i] 表示从左到右跳到i的最长sequence 的长度

        # initialization: dp[0..n-1] = 1
        dp = [1] * len(nums)

        # prev[i] 代表 dp[i] 的最优值是从哪个 dp[j] 算过来的
        prev = [-1] * len(nums)

        # function dp[i] = max{dp[j] + 1},  j < i and nums[j] < nums[i]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        # answer: max(dp[0..n-1])
        longest, last = 0, -1
        for i in range(len(nums)):
            if dp[i] > longest:
                longest = dp[i]
                last = i

        path = []
        while last != -1:
            path.append(nums[last])
            last = prev[last]
        print(path[::-1])


    def longestIncreasingSubsequenceOptimize(self, nums):
        if not nums:
            return 0
        m = len(nums)
        dp = [0] * m
        # dp[size-1] contains the last value of the longest sequence.
        dp[0] = nums[0]
        size = 1
        for num in nums:
            insertion_point = bisect.bisect_left(dp, num, 0, size)
            dp[insertion_point] = num
            if insertion_point == size:
                size += 1
        # dp[0:size] is the longest sequence!!!
        print(dp[0:size])
        return size

if __name__ == '__main__':
    s = Solution()
    s.longestIncreasingSubsequenceOptimize([5,4,1,2,3])