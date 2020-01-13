class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end])

    def findMin2(self, nums):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if mid == end:
                # this is the case where there is only one element left
                # so the only element is the solution
                return nums[mid]
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                # when nums[mid] < nums[end]
                # nums[mid] could be the minimum value
                end = mid
        return min(nums[start], nums[end])


if __name__ == '__main__':
    s = Solution()
    s.findMin2([4,5,6,7,8,9,1,2,3])