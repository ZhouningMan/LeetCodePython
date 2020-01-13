class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        if not nums:
            return 0.0
        size = sum(len(arr) for arr in nums)
        if size == 0:
            return 0.0
        start, end = self.find_range(nums)
        if size % 2 == 1:  # odd number of items
            return self.find_kth(nums, size // 2 + 1, start, end)
        return (self.find_kth(nums, size // 2, start, end)
                + self.find_kth(nums, size // 2 + 1, start, end)) / 2

    def find_range(self, nums):
        start = min(arr[0] for arr in nums if len(arr))
        end = max(arr[-1] for arr in nums if len(arr))
        return start, end

    # kth is one-based
    def find_kth(self, nums, k, start, end):
        # this is important, find the kth value in a sorted list using binary search
        # using range
        while start + 1 < end:
            mid = (start + end) // 2
            if self.find_smaller_or_equal(nums, mid) >= k:
                end = mid
            else:
                start = mid
        if self.find_smaller_or_equal(nums, start) >= k:
            return start
        return end

    def find_smaller_or_equal(self, nums, target):
        count = 0
        # this is to use index
        for arr in nums:
            if len(arr) == 0:
                continue
            start = 0
            end = len(arr) - 1
            while start + 1 < end:
                mid = (start + end) // 2
                if arr[mid] > target:
                    end = mid
                else:
                    start = mid
            if arr[start] > target: # the index is zero based, so we can't do >=
                count += start
            elif arr[end] > target:
                count += end
            else:
                count += end + 1  # everything is less than target
        return count


if __name__ == '__main__':
    print(Solution().findMedian([[1],[2],[3]]))