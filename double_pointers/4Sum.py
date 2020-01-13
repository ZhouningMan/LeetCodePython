class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        if not numbers or len(numbers) < 4:
            return []
        size = len(numbers)
        ans = []
        numbers.sort()
        for i in range(size - 3):
            # dedup
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, size - 2):
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                left = j + 1
                right = size - 1
                while left < right:
                    # dedup
                    if left > j + 1 and numbers[left] == numbers[left - 1]:
                        left += 1
                        continue
                    s = numbers[left] + numbers[right] + numbers[i] + numbers[j]
                    if s == target:
                        ans.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return ans

if __name__ == '__main__':
    s = Solution()
    ans = s.fourSum([-5,-3,-2,1,2,2,3,4,9], 1)
    print(ans)