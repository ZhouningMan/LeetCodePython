class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        if nums is None or len(nums) == 0 or k > len(nums):
            return -1
        start = 0
        end = len(nums) - 1
        # quick select is not binary search, we CANNOT use the
        # template from the binary search problem
        while start <= end:
            i = self.partition3(nums, start, end)
            if i + 1 == k:
                return nums[i]
            elif i + 1 < k:
                start = i + 1
            else:
                end = i - 1
        return -1

    def partition(self, nums, start, end):
        if start >= end:
            return start
        pivot = nums[start]
        i = start + 1
        j = end
        while i <= j:  # don't do extra comparison if our condition is met
            # i don't do <= or >= is to make sure
            # this partition works well for mostly same elemetns
            while i <= j and nums[i] < pivot:
                i += 1
            while j >= i and nums[j] > pivot:
                j -= 1
            if i <= j:
                self.swap(nums, i, j)
                # we have to have the following statements when we are not using equal sign
                i += 1
                j -= 1
        self.swap(nums, start, j) # deal with corner cases.
        return j  # this is the answer.


    def partition2(self, nums, start, end):
        if start >= end:
            return start
        self.swap(nums, start, (start + end) // 2)
        pivot = nums[start]
        i = start + 1
        j = end
        while i <= j:  # don't do extra comparison if our condition is met
            if nums[i] > pivot:
                self.swap(nums, i, j)
                j -= 1
            else:
                i += 1
        self.swap(nums, start, j) # deal with corner cases.
        return j  # this is the answer.
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    print(Solution().kthSmallest(3, [9,3,2,4,8]))