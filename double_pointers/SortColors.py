class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        if not nums:
            return 0
        i = 0
        ri = len(nums) - 1
        le = 0
        # nums[le, ri] are equals
        while i <= ri:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                nums[le], nums[i] = nums[i], nums[le]
                le += 1
                i += 1
            else:
                nums[i], nums[ri] = nums[ri], nums[i]
                ri -= 1
        print(f"le={le}, ri={ri}")

if __name__ == '__main__':
    s = Solution()
    A = [0, 0, 2]
    s.sortColors(A)
    print(A)