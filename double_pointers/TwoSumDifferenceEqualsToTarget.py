from collections import defaultdict

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        if not nums or len(nums) < 2:
            return None
        val_2_idx = defaultdict(list)
        for i, v in enumerate(nums):
            val_2_idx[v].append(i)

        for i, v in enumerate(nums):
            if v - target not in val_2_idx:
                continue
            idx = val_2_idx[v - target]
            for j in idx:
                if j == i:
                    continue
                return [min(i, j) + 1, max(i, j) + 1]
        return None


if __name__ == '__main__':
    s = Solution()
    ans = s.twoSum7([1,0,1], 0)
    print(ans)