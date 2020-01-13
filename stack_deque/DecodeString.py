class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        if not s or len(s) == 0:
            return ""

        prefix = []
        counts = []
        chars = ""
        count = 0
        for c in s:
            if c.isdigit():
                count = count * 10 + int(c)
            elif c == '[':  # event to push
                prefix.append(chars)
                counts.append(count)
                # once you push the content, you want to reset it
                # we make it very easy, every count is always accompanies by
                # a prefix
                count = 0
                chars = ""
            elif c == ']':
                # the internal chars is what is multiplied
                chars = chars * counts.pop()
                # and add the prefix back
                chars = prefix.pop() + chars
            else:
                chars += c
        return chars


if __name__ == '__main__':
    s = Solution()
    print(s.expressionExpand("abc3[a]"))