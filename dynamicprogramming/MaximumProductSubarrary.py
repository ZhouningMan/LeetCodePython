class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        if not nums:
            return 0
        max_prod = nums[0]
        min_prod = nums[0]
        answer = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            elements = [num, max_prod * num, min_prod * num]
            max_prod = max(elements)
            min_prod = min(elements)
            answer = max(answer, max_prod)
        return answer
