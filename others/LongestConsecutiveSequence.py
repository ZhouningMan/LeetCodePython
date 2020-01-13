class Solution:
    def longest_consecutive(self, nums) -> int:
        nums_set = set(nums)
        longest = 0
        for n in nums:
            if n not in nums_set:
                continue
            nums_set.remove(n)
            left = n
            right = n
            while left - 1 in nums_set:
                left -= 1
                nums_set.remove(left)
            while right + 1 in nums_set:
                right += 1
                nums_set.remove(right)
            longest = max(longest, right - left + 1)

        return longest


if __name__ == '__main__':
    res = Solution().longest_consecutive([100, 4, 200, 1, 3, 2])
    print(res)