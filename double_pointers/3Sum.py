class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        if not numbers:
            return []
        size = len(numbers)
        if size < 3:
            return []
        numbers.sort()
        ans = []
        for i in range(size - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            if numbers[i] > 0:
                break
            left = i + 1
            right = size - 1
            target = -numbers[i]
            while left < right: # I cannot use equal sign
                if left > i + 1 and numbers[left] == numbers[left - 1]:
                    left += 1
                    continue
                s = numbers[left] + numbers[right]
                if s == target:
                    ans.append([numbers[i], numbers[left], numbers[right]])
                    # i cannot just break here
                    left += 1
                    right -= 1
                elif s > target:
                    right -= 1
                else:
                    left += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    ans = s.threeSum([1,0,-1,-1,-1,-1,0,1,1,1])