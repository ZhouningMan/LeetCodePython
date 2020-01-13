
class Solution:
    count = 0
    def shortestSuperstring(self, A) -> str:
        return self.dfs("", A)

    def dfs(self, ss, words):
        Solution.count += 1
        print("\t" * Solution.count + f"prefix = {ss}")
        if not words:
            Solution.count -= 1
            return ss
        ans = None
        for i in range(len(words)):
            if words[i] not in ss:
                tmp = self.dfs(ss + words[i], words[:i] + words[i + 1:])
            else:
                tmp = self.dfs(ss, words[:i] + words[i + 1:])
            if not ans:
                ans = tmp
            else:
                ans = min(ans, tmp, key=len)
        Solution.count -= 1

        return ans


if __name__ == '__main__':
    s = Solution()
    ans = s.shortestSuperstring(["catg","ctaagt","gcta","ttca","atgcatc"])
    print(ans)