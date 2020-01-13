class Solution:
    def expand(self, S: str) -> List[str]:
        if not S:
            return []
        begin = self.index(S, 0, '{')
        prefix = {S[:begin]}
        # the unit of work in this problem is
        # prefix * options within {} * suffixes
        # ths is a simple problem because we don't have nested {}
        while begin < len(S):
            end = self.index(S, begin, '}')
            inStr = S[begin + 1: end]
            options = inStr.split(',')
            begin = self.index(S, end, '{')
            suffix = {S[end + 1: begin]}
            prefix = self.product(self.product(prefix, options), suffix)
        return sorted(prefix)

    def index(self, S, begin, char):
        for i in range(begin, len(S)):
            if S[i] == char:
                return i
        return len(S)

    def product(self, prefix, options):
        result = set()
        for i in prefix:
            for j in options:
                result.add(i + j)
        return result

