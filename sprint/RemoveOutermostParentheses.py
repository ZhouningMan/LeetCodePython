from collections import deque

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = ""
        stack = []
        for i, c in enumerate(S):
            if c == '(':
                stack.append(i)
            elif len(stack) == 1:
                begin = stack.pop()
                ans += S[begin+1:i]
            else:
                stack.pop()
        return ans