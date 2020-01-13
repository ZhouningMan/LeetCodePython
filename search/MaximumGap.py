class Solution:
    """
    @param nums: an array of integers
    @return: the maximun difference
    """
    def maximumGap(self, nums):
        if not nums or len(nums) <= 1:
            return 0
        self.radix_sort(nums)
        gap = 0
        for i in range(1, len(nums)):
            gap = max(nums[i] - nums[i-1], gap)
        return gap

    def radix_sort(self, nums):
        m = len(nums)
        aux = [0] * m

        def get_key(num, i):
            if i < 3:
                return (num >> i * 8) & 0xFF
            else:
                # Great way to compare the signed byte values
                # just by adding 128 to each signed byte
                return ((num >> i * 8) + 0x80) & 0xFF

        radix = 256
        for i in range(4):
            count = [0] * (radix + 1)
            for j in range(m):  # count the keys
                key = get_key(nums[j], i)
                # use the key as an index in the count array
                count[key + 1] += 1
            for r in range(radix):  # add the cumulates of keys
                count[r + 1] += count[r]
            for j in range(m):
                # use the key as an index to the count array
                key = get_key(nums[j], i)
                aux[count[key]] = nums[j]
                # for the same key move to the next position
                count[key] += 1
            for j in range(m):
                # copy back
                nums[j] = aux[j]

if __name__ == '__main__':
    s = Solution()
    nums = [2147483647, 0]
    gap = s.maximumGap(nums)
    print(gap)