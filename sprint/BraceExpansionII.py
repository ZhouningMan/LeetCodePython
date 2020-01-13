class Solution:
    def braceExpansionII(self, expression):
        if not expression:
            return []
        print(expression)
        begin = self.index(expression, 0, '{')
        prefix = {expression[:begin]}
        # the unit of work in this problem is
        # prefix * options within {} * suffixes
        # ths is a simple problem because we don't have nested {}
        while begin < len(expression):
            end = self.findMatchingBrace(expression, begin)
            inStr = expression[begin + 1: end]
            options = inStr.split(',')
            words = []
            for option in options:
                words += self.braceExpansionII(option)
            begin = self.index(expression, end, '{')
            suffix = {expression[end + 1: begin]}
            prefix = self.product(self.product(prefix, set(words)), suffix)
        return sorted(prefix)

    def findMatchingBrace(self, expression, begin):
        count = 0
        for i in range(begin, len(expression)):
            if expression[i] == '{':
                count += 1
            elif expression[i] == '}':
                count -= 1
            if count == 0:
                return i
        return -1

    def index(self, expression, begin, char):
        for i in range(begin, len(expression)):
            if expression[i] == char:
                return i
        return len(expression)

    def product(self, prefix, options):
        result = set()
        for i in prefix:
            for j in options:
                result.add(i + j)
        return result

if __name__ == '__main__':
    s = Solution()
    ans = s.braceExpansionII("{{a, b}{c, {d, e}}}")
    print(ans)


