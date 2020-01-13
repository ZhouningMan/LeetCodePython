MAPPINGS = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

rotation = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
class Solution:
    def confusingNumberII(self, N: int) -> int:
        count = 0
        for i in [1, 6, 8, 9]:
            count += self.dfs(i, N)
        return count

    def dfs(self, val, N):
        if val > N:
            return 0
        count = 0
        if self.confusingNumber(val):
            count += 1
        for i in MAPPINGS.keys():
            tmp = val * 10 + i
            count += self.dfs(tmp, N)
        return count

    def confusingNumber(self, N):
        S = str(N)
        result = []
        for c in S[::-1]:  # iterate in reverse
            if c not in rotation:
                return False
            result.append(rotation[c])
        return "".join(result) != S


if __name__ == '__main__':
    s = Solution()
    ans = s.confusingNumberII(20)
    print(ans)