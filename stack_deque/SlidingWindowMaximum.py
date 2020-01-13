import collections


class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        if not nums or len(nums) < k:
            return []

        window = collections.deque()
        result = []
        for i, val in enumerate(nums):
            # we are building a monotonously decreasing stack
            while len(window) > 0 and nums[window[-1]] < val:
                window.pop()
            window.append(i)
            # remove the tail if it is out side the window
            if window[-1] - window[0] >= k:
                window.popleft()
            if i >= k - 1:
                result.append(nums[window[0]])
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.maxSlidingWindow([1,2,7,7,2,10,3,4,5], 2)
    print(res)