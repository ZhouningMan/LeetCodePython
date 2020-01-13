class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        if not nums:
            return 0
        unique_nums = set()
        start = 0
        end = len(nums) - 1

        # don't maintain relative order
        while start <= end:
            if nums[start] in unique_nums:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                unique_nums.add(nums[start])
                start += 1
        return end + 1

    def deduplication2(self, nums):
        if not nums:
            return 0
        unique_nums = set()
        dup_count = 0
        for i, val in enumerate(nums):
            if val in unique_nums:
                dup_count += 1
            else:
                unique_nums.add(val)
                nums[i], nums[i-dup_count] = nums[i-dup_count], nums[i]
        return len(nums) - dup_count