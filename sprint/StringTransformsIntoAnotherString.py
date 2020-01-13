class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        if str1 == str2:
            return True

        mappings = {}
        for i in range(len(str1)):
            c1 = str1[i]
            c2 = str2[i]
            if c1 not in mappings:
                mappings[c1] = c2
            elif mappings[c1] != c2:
                return False
        if len(set(mappings.values())) >= 26:
            return False
        else:
            return True

    def checkCycle(self, mappings):
        visited = set()
        for key in mappings.keys():
            if key in visited:
                continue
            if self.found(key, mappings, visited):
                return True
        return False

    def found(self, key, mappings, visited):
        if key not in mappings:
            return False
        if key in visited:
            return True
        visited.add(key)
        nk = mappings[key]
        return self.found(nk, mappings, visited)

if __name__ == '__main__':
    s = Solution()
    print(s.canConvert("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxzy"))