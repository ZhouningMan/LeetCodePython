class Solution:
    def findDuplicate(self, nums):
        # binary counting
        low = 1  # smallest number is 1
        high = len(nums) - 1  # largest number is n
        while low < high:
            # this mid is the value not, the index
            mid = low + (high - low)//2
            count = 0
            # during each iteration we loop through the entire list
            for i in nums:  # loop through each value
                if i <= mid:
                    count += 1
            if count > mid:  # more numbers than mid
                high = mid
            else:
                low = mid + 1

        return low

    def find_duplicate_floyd_tortoise_hare(self, nums):
        tortoise = nums[0]
        hare = nums[0]
        # This is basically a do-while loop because the first element is always going to be the
        # same
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # reset the loop, the first position could be the beginning of the loop
        # so we want to start the condition check right away
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return tortoise
