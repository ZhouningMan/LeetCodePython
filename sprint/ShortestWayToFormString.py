import bisect

class Solution:
    def shortestWay(self, source, target):
        scIndice = self.buildCharIndices(source)
        prev = -1
        ans = 0
        for c in target:
            if c not in scIndice:
                return -1
            indices = scIndice[c]
            idx = bisect.bisect_right(indices, prev)
            if idx == len(indices):
                ans += 1
                # i should not initialize this to -1 because
                # I need to remember the index of current character in the source string
                prev = indices[0]
            else:
                # i need to assigned the index of current character in the source string
                # to previous, NOT the index of the index array
                prev = indices[idx]
        ans += 1
        return ans

    def buildCharIndices(self, source):
        charsInices = {}
        for i, c in enumerate(source):
            if c not in charsInices:
                charsInices[c] = []
            charsInices[c].append(i)
        return charsInices

if __name__ == '__main__':
    s = Solution()
    ans = s.shortestWay("xyz", "xzyxz")
    print(ans)