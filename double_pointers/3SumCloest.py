MAX_INT = 2**63 - 1
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        if not numbers or len(numbers) < 3:
            raise ValueError("Invalid arguments...")
        size = len(numbers)
        numbers.sort()
        diff = MAX_INT
        ans = target
        for i in range(size - 2):
            temp = target - numbers[i]  # change three sum to 2 sum
            left = i + 1
            right = size - 1
            while left < right:  # double pointers
                s = numbers[left] + numbers[right]
                if abs(s - temp) < diff:  # better candidate is found
                    ans = numbers[i] + numbers[left] + numbers[right]
                    diff = abs(s - temp)
                if s == temp:
                    return ans
                elif s < temp:
                    left += 1
                else:
                    right -= 1
        return ans


